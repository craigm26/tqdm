"""
Progress bars that behave in CI logs.

`ci_tqdm` is a drop-in `tqdm` that stays quiet when it runs in CI
(the `CI` environment variable is set) and stderr isn't a terminal,
so build logs aren't filled with carriage-return redraws.
"""
import os
import sys

from ..std import tqdm

__all__ = ['ci_tqdm', 'in_ci']


def in_ci(environ=None, stream=None):
    """True when running in CI without a terminal attached."""
    environ = os.environ if environ is None else environ
    stream = sys.stderr if stream is None else stream
    if environ.get("CI", "").lower() not in ("1", "true", "yes"):
        return False
    isatty = getattr(stream, "isatty", None)
    return not (isatty and isatty())


class ci_tqdm(tqdm):  # pylint: disable=invalid-name
    """`tqdm` that disables itself in CI unless `disable` is given."""

    def __init__(self, *args, **kwargs):
        if "disable" not in kwargs:
            kwargs["disable"] = in_ci(stream=kwargs.get("file"))
        super().__init__(*args, **kwargs)
