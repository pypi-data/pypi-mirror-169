#!/usr/bin/env python3
# Copyright (c) 2021-2022 Ryan Moore
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""# ty 🦆
`usage: ty [-h|--help] [-q] [...] [file.py] [...]`

A configurable type-checking Python command. Runs the configured type checker
before (possibly) executing Python.

## Install
```
pip install ty-command
```

## Typical usage examples
```
$ ty            # same as `python3 -m mypy .`
$ ty file.py    # same as `python3 -m mypy .` + `python3 file.py`
```

Optional `pyproject.toml` file to configure type checker:
```
[tool.ty]
type_checker = "pyright" # "mypy" is the default, "pytype" also available
```

## Tip
Did you know `python3 -` opens the terminal? `ty -` does too, and it type checks!
"""

# NOTE I'd like this file to be useful by itself without any auxiliary files.
#      That's also why I'm not naming it main.py.

import sys
from subprocess import CompletedProcess, run
from typing import List, NoReturn

import tomli


class TyError(Exception):
    pass


def _pyproject_toml() -> str:
    # TODO what about in above dirs?
    #      for example im in /pkg/src and there's no pyproject.toml
    #      figure out how Black acts and copy that
    return "./pyproject.toml"


def _type_checker() -> str:
    with open(_pyproject_toml(), "r") as f:
        toml = f.read()

    # TODO Use built-in if available and tomli if not
    try:
        type_checker = tomli.loads(toml)["tool"]["ty"]["type_checker"]
    except:  # TODO whats the exception
        return "mypy"
    assert type(type_checker) == str
    return type_checker


def _python() -> str:
    # TODO check for `py` then `python3` then `python` command?
    #      if I return sys.executable, that means you *cant* offer a version
    #      string like py -3.6 but I like this feature so I should fix this
    return sys.executable


def _run_python(argv: List[str]) -> CompletedProcess[bytes]:
    cmd = [_python(), *argv]
    return run(cmd)


def _run_type_checker(checker: str) -> CompletedProcess[bytes]:
    supported_type_checkers = ["mypy", "pyright", "pytype"]
    if checker not in supported_type_checkers:
        raise TyError(
            f"Checker `{checker}` is not a supported type checker: \
            `{supported_type_checkers}`!"
        )
    # TODO logic individual
    # TODO quiet logic
    cmd = [_python(), "-m", checker, "."]
    return run(cmd)


def _return_code(process: CompletedProcess[bytes]) -> int:
    return process.returncode


def _help_message(executable: str) -> str:
    msg = f"""\
    {__doc__}

    The following help text is from {executable}:
    {_run_python(["--help"])}
    """
    return msg


def _execute_python(argv: List[str]) -> int:
    # TODO look at:
    # https://docs.python.org/3/library/os.html?highlight=os%20execve#os.execve
    if False:  # TODO help condition
        # lets react to help flags the same way py does
        # $ py --help 1
        # The `--help` flag must be specified on its own; see `py --help` for details
        # $ py -h 1
        # The `-h` flag must be specified on its own; see `py --help` for details
        # $ py 1 -h
        # /opt/homebrew/Cellar/python@3.10/3.10.5/bin/python3.10: can't open file
        # '/Users/ryan/ty/1': [Errno 2] No such file or directory
        sys.stderr.write(_help_message())
    return _return_code(_run_python(argv))


def _execute_type_checker(checker: str) -> int:
    return _return_code(_run_type_checker(checker))


def _ty(argv: List[str]) -> int:
    type_checker = _type_checker()
    # TODO sys.exit treating the two commands as one basically
    #      early out if error like
    if (type_status := _execute_type_checker(type_checker)) != 0:
        return type_status
    if len(argv) == 0:
        return 0
    return _execute_python(argv)


def ty() -> NoReturn:
    sys.exit(_ty(sys.argv[1:]))


if __name__ == "__main__":
    # For when script is used as a Python file, not pip installed CLI command
    ty()
