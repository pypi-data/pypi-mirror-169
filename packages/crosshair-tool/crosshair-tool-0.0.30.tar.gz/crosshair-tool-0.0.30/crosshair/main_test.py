import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from argparse import Namespace
from os.path import join, split

import pytest

from crosshair.fnutil import NotFound
from crosshair.main import (
    DEFAULT_OPTIONS,
    AnalysisKind,
    AnalysisMessage,
    AnalysisOptionSet,
    List,
    MessageType,
    Path,
    Tuple,
    check,
    describe_message,
    diffbehavior,
    set_debug,
    textwrap,
    unwalled_main,
    watch,
)
from crosshair.test_util import simplefs
from crosshair.util import add_to_pypath, load_file


@pytest.fixture(autouse=True)
def rewind_modules():
    defined_modules = list(sys.modules.keys())
    yield None
    for name, module in list(sys.modules.items()):
        # Some standard library modules aren't happy with getting reloaded.
        if name.startswith("multiprocessing"):
            continue
        if name not in defined_modules:
            del sys.modules[name]


def call_check(
    files: List[str], options: AnalysisOptionSet = AnalysisOptionSet()
) -> Tuple[int, List[str], List[str]]:
    stdbuf: io.StringIO = io.StringIO()
    errbuf: io.StringIO = io.StringIO()
    retcode = check(Namespace(target=files), options, stdbuf, errbuf)
    stdlines = [ls for ls in stdbuf.getvalue().split("\n") if ls]
    errlines = [ls for ls in errbuf.getvalue().split("\n") if ls]
    return retcode, stdlines, errlines


def call_diffbehavior(fn1: str, fn2: str) -> Tuple[int, List[str]]:
    buf: io.StringIO = io.StringIO()
    errbuf: io.StringIO = io.StringIO()
    retcode = diffbehavior(Namespace(fn1=fn1, fn2=fn2), DEFAULT_OPTIONS, buf, errbuf)
    lines = [
        ls for ls in buf.getvalue().split("\n") + errbuf.getvalue().split("\n") if ls
    ]
    return retcode, lines


SIMPLE_FOO = {
    "foo.py": """
def foofn(x: int) -> int:
  ''' post: _ == x '''
  return x + 1
"""
}

FOO_CLASS = {
    "foo.py": """
class Fooey:
  def incr(self, x: int) -> int:
    ''' post: _ == x '''
    return x + 1
"""
}
ASSERT_BASED_FOO = {
    "foo.py": """
def foofn(x: int) -> int:
  ''' :raises KeyError: when input is 999 '''
  assert x >= 100
  x = x + 1
  if x == 1000:
      raise KeyError
  assert x != 101
  return x
"""
}

FOO_WITH_CONFIRMABLE_AND_PRE_UNSAT = {
    "foo.py": """
def foo_confirmable(x: int) -> int:
  ''' post: _ > x '''
  return x + 1
def foo_pre_unsat(x: int) -> int:
  '''
  pre: x != x
  post: True
  '''
  return x
"""
}

OUTER_INNER = {
    "outer": {
        "__init__.py": "",
        "inner.py": """
def foofn(x: int) -> int:
  ''' post: _ == x '''
  return x
""",
    }
}

CIRCULAR_WITH_GUARD = {
    "first.py": """
import typing
if typing.TYPE_CHECKING:
    from second import Second
class First():
    def __init__(self, f: "Second") -> None:
        ''' post: True '''
""",
    "second.py": """
from first import First
class Second():
    pass
""",
}


DIRECTIVES_TREE = {
    "outerpkg": {
        "__init__.py": "# crosshair: off",
        "outermod.py": textwrap.dedent(
            """\
            def fn1():
                assert True
                raise Exception
            """
        ),
        "innerpkg": {
            "__init__.py": "# crosshair: on",
            "innermod.py": textwrap.dedent(
                """\
                # crosshair: off
                def fn2():
                    # crosshair: on
                    assert True
                    raise Exception  # this is the only function that's enabled
                def fn3():
                    assert True
                    raise Exception
                """
            ),
        },
    }
}


class MainTest(unittest.TestCase):
    # TODO convert all to pytest; "rewind_modules" fixture above will handle teardown

    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        self.defined_modules = list(sys.modules.keys())

    def tearDown(self):
        shutil.rmtree(self.root)
        defined_modules = self.defined_modules
        for name, module in list(sys.modules.items()):
            # Some standard library modules aren't happy with getting reloaded.
            if name.startswith("multiprocessing"):
                continue
            if name not in defined_modules:
                del sys.modules[name]

    def test_load_file(self):
        simplefs(self.root, SIMPLE_FOO)
        module = load_file(join(self.root, "foo.py"))
        self.assertNotEqual(module, None)
        self.assertEqual(module.foofn(5), 6)

    def test_check_by_filename(self):
        simplefs(self.root, SIMPLE_FOO)
        retcode, lines, _ = call_check([str(self.root / "foo.py")])
        self.assertEqual(retcode, 1)
        self.assertEqual(len(lines), 1)
        self.assertIn("foo.py:3: error: false when calling foofn", lines[0])

    def test_check_by_class(self):
        simplefs(self.root, FOO_CLASS)
        with add_to_pypath(self.root):
            retcode, lines, _ = call_check(["foo.Fooey"])
            self.assertEqual(retcode, 1)
            self.assertEqual(len(lines), 1)
            self.assertIn("foo.py:4: error: false when calling incr", lines[0])

    def test_check_failure_via_main(self):
        simplefs(self.root, SIMPLE_FOO)
        try:
            sys.stdout = io.StringIO()
            self.assertEqual(1, unwalled_main(["check", str(self.root / "foo.py")]))
        finally:
            sys.stdout = sys.__stdout__

    def test_check_ok_via_main(self):
        # contract is assert-based, but we do not analyze that type.
        simplefs(self.root, ASSERT_BASED_FOO)
        try:
            sys.stdout = io.StringIO()
            exitcode = unwalled_main(
                [
                    "check",
                    str(self.root / "foo.py"),
                    "--analysis_kind=PEP316,icontract",
                ]
            )
            self.assertEqual(exitcode, 0)
        finally:
            sys.stdout = sys.__stdout__

    def test_no_args_prints_usage(self):
        try:
            sys.stderr = io.StringIO()
            exitcode = unwalled_main([])
        finally:
            out = sys.stderr.getvalue()
            sys.stderr = sys.__stderr__
        self.assertEqual(exitcode, 2)
        self.assertRegex(out, r"^usage")

    def DISABLE_TODO_test_assert_mode_e2e(self):
        simplefs(self.root, ASSERT_BASED_FOO)
        try:
            sys.stdout = io.StringIO()
            exitcode = unwalled_main(
                ["check", self.root / "foo.py", "--analysis_kind=asserts"]
            )
        finally:
            out = sys.stdout.getvalue()
            sys.stdout = sys.__stdout__
        self.assertEqual(exitcode, 1)
        self.assertRegex(
            out, r"foo.py\:8\: error\: AssertionError\:  when calling foofn\(x \= 100\)"
        )
        self.assertEqual(len([ls for ls in out.split("\n") if ls]), 1)

    def test_directives(self):
        simplefs(self.root, DIRECTIVES_TREE)
        ret, out, err = call_check(
            [str(self.root)], AnalysisOptionSet(analysis_kind=[AnalysisKind.asserts])
        )
        self.assertEqual(err, [])
        self.assertEqual(ret, 1)
        self.assertRegex(
            out[0], r"innermod.py:5: error: Exception:  when calling fn2()"
        )
        self.assertEqual(len(out), 1)

    def test_directives_on_check_with_linenumbers(self):
        simplefs(self.root, DIRECTIVES_TREE)
        ret, out, err = call_check(
            [str(self.root / "outerpkg" / "innerpkg" / "innermod.py") + ":5"],
            AnalysisOptionSet(analysis_kind=[AnalysisKind.asserts]),
        )
        self.assertEqual(err, [])
        self.assertEqual(ret, 1)
        self.assertRegex(
            out[0], r"innermod.py:5: error: Exception:  when calling fn2()"
        )
        self.assertEqual(len(out), 1)

    def test_report_confirmation(self):
        simplefs(self.root, FOO_WITH_CONFIRMABLE_AND_PRE_UNSAT)
        retcode, lines, _ = call_check([str(self.root / "foo.py")])
        self.assertEqual(retcode, 0)
        self.assertEqual(lines, [])
        # Now, turn on confirmations with the `--report_all` option:
        retcode, lines, _ = call_check(
            [str(self.root / "foo.py")], options=AnalysisOptionSet(report_all=True)
        )
        self.assertEqual(retcode, 0)
        self.assertEqual(len(lines), 2)
        output_text = "\n".join(lines)
        self.assertIn("foo.py:3: info: Confirmed over all paths.", output_text)
        self.assertIn("foo.py:7: info: Unable to meet precondition.", output_text)

    def test_check_nonexistent_filename(self):
        simplefs(self.root, SIMPLE_FOO)
        retcode, _, errlines = call_check([str(self.root / "notexisting.py")])
        self.assertEqual(retcode, 2)
        self.assertEqual(len(errlines), 1)
        self.assertIn("File not found", errlines[0])
        self.assertIn("notexisting.py", errlines[0])

    def test_check_by_module(self):
        simplefs(self.root, SIMPLE_FOO)
        with add_to_pypath(self.root):
            retcode, lines, _ = call_check(["foo"])
            self.assertEqual(retcode, 1)
            self.assertEqual(len(lines), 1)
            self.assertIn("foo.py:3: error: false when calling foofn", lines[0])

    def test_check_nonexistent_module(self):
        simplefs(self.root, SIMPLE_FOO)
        retcode, _, errlines = call_check(["notexisting"])
        self.assertEqual(retcode, 2)
        self.assertEqual(
            "crosshair.fnutil.NotFound: Module 'notexisting' was not found",
            errlines[-1],
        )

    def test_check_by_package(self):
        simplefs(self.root, OUTER_INNER)
        with add_to_pypath(self.root):
            retcode, lines, _ = call_check(["outer.inner.foofn"])
            self.assertEqual(retcode, 0)
            self.assertEqual(len(lines), 0)

    def test_check_nonexistent_member(self):
        simplefs(self.root, OUTER_INNER)
        with add_to_pypath(self.root):
            self.assertRaises(NotFound, lambda: call_check(["outer.inner.nonexistent"]))

    def test_check_circular_with_guard(self):
        simplefs(self.root, CIRCULAR_WITH_GUARD)
        with add_to_pypath(self.root):
            retcode, lines, _ = call_check([str(self.root / "first.py")])
            self.assertEqual(retcode, 0)

    def test_watch(self):
        # Just to make sure nothing explodes
        simplefs(self.root, SIMPLE_FOO)
        retcode = watch(
            Namespace(directory=[str(self.root)]),
            AnalysisOptionSet(),
            max_watch_iterations=2,
        )
        self.assertEqual(retcode, 0)

    def test_diff_behavior_same(self):
        simplefs(self.root, SIMPLE_FOO)
        with add_to_pypath(self.root):
            retcode, lines = call_diffbehavior("foo.foofn", str(self.root / "foo.py:2"))
            self.assertEqual(
                lines,
                [
                    "No differences found. (attempted 2 iterations)",
                    "All paths exhausted, functions are likely the same!",
                ],
            )
            self.assertEqual(retcode, 0)

    def test_diff_behavior_different(self):
        simplefs(
            self.root,
            {
                "foo.py": """
def add(x: int, y: int) -> int:
  return x + y
def faultyadd(x: int, y: int) -> int:
  return 42 if (x, y) == (10, 10) else x + y
"""
            },
        )
        with add_to_pypath(self.root):
            retcode, lines = call_diffbehavior("foo.add", "foo.faultyadd")
            self.assertEqual(retcode, 1)
            self.assertEqual(
                lines,
                [
                    "Given: (x=10, y=10),",
                    "        foo.add : returns 20",
                    "  foo.faultyadd : returns 42",
                ],
            )

    def test_diff_behavior_error(self):
        retcode, lines = call_diffbehavior("foo.unknown", "foo.unknown")
        self.assertEqual(retcode, 2)
        self.assertRegex(lines[0], ".*NotFound")

    def test_diff_behavior_targeting_error(self):
        simplefs(self.root, SIMPLE_FOO)
        with add_to_pypath(self.root):
            retcode, lines = call_diffbehavior("foo.foofn", "foo")
            self.assertEqual(retcode, 2)
            self.assertEqual(lines, ['"foo" does not target a function.'])

    def test_diff_behavior_via_main(self):
        simplefs(self.root, SIMPLE_FOO)
        sys.stdout = io.StringIO()
        try:
            with add_to_pypath(self.root):
                self.assertEqual(
                    0, unwalled_main(["diffbehavior", "foo.foofn", "foo.foofn"])
                )
        finally:
            out = sys.stdout.getvalue()
            sys.stdout = sys.__stdout__
        self.assertRegex(out, "No differences found")


def test_cover(tmp_path: Path, capsys: pytest.CaptureFixture[str]):
    simplefs(tmp_path, SIMPLE_FOO)
    with add_to_pypath(str(tmp_path)):
        assert unwalled_main(["cover", "foo.foofn"]) == 0
    assert capsys.readouterr().out == "foofn(0)\n"


def test_main_as_subprocess(tmp_path: Path):
    # This helps check things like addaudithook() which we don't want to run inside
    # the testing process.
    simplefs(tmp_path, SIMPLE_FOO)
    completion = subprocess.run(
        ["python", "-m", "crosshair", "check", str(tmp_path)],
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
    )
    assert completion.returncode == 1
    assert "foo.py:3: error: false when calling foofn" in completion.stdout
    assert completion.stderr == ""


def test_mypycrosshair_command():
    example_file = join(
        split(__file__)[0], "examples", "icontract", "bugs_detected", "wrong_sign.py"
    )
    completion = subprocess.run(
        [
            f"python",
            f"-c",
            f"import crosshair.main;"
            + f"crosshair.main.mypy_and_check([r'{example_file}'])",
        ],
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
    )
    assert completion.stderr.strip() == ""
    assert completion.returncode == 1


def test_describe_message():
    msg = AnalysisMessage(MessageType.PRE_UNSAT, "unsat", "filename", 1, 1, "traceback")
    opts = DEFAULT_OPTIONS.overlay(report_all=True, report_verbose=True)
    assert describe_message(msg, opts).split("\n") == [
        "traceback",
        "\x1b[91mI am having trouble finding any inputs that meet your preconditions.\x1b[0m",
        "filename:1:",
        "",
        "unsat",
        "",
    ]


if __name__ == "__main__":
    if ("-v" in sys.argv) or ("--verbose" in sys.argv):
        set_debug(True)
    unittest.main()
