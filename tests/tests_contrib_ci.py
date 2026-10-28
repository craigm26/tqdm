from io import StringIO

from tqdm.contrib.ci import ci_tqdm, in_ci


class TTY(StringIO):
    def isatty(self):
        return True


def test_in_ci_needs_ci_variable():
    assert not in_ci(environ={}, stream=StringIO())
    assert in_ci(environ={"CI": "true"}, stream=StringIO())


def test_in_ci_false_on_a_terminal():
    assert not in_ci(environ={"CI": "true"}, stream=TTY())


def test_ci_tqdm_quiet_in_ci(monkeypatch):
    monkeypatch.setenv("CI", "true")
    out = StringIO()
    for _ in ci_tqdm(range(3), file=out):
        pass
    assert out.getvalue() == ""


def test_ci_tqdm_explicit_disable_wins(monkeypatch):
    monkeypatch.setenv("CI", "true")
    out = StringIO()
    for _ in ci_tqdm(range(3), file=out, disable=False):
        pass
    assert "3/3" in out.getvalue()
