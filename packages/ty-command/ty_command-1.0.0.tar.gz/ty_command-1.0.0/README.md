# ty 🦆
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
