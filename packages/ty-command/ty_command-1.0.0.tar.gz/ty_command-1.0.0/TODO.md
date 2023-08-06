# Version 0.

## Problems:
- [x] When entering the terminal with `ty -`, black isort and the type checker should run. If they didn't run it would offer no benefit to using `py` and sometimes I want to test something in a terminal and running the suite would be helpful to not import something with type errors in the tty.
- [ ] If `ty` is used to run a file in a different folder, it uses the default `mypy`
because it can't find a `pyproject.toml` in the `$(realpath dirname $PWD)`. Should it do this? Is it possible to find what module a script belongs to?
What happens for namespace packages?
- [ ] Fix the paths in the tests folders using new `example` path

# Version 1.

## Goals:

- [x] Just one file, this whole thing should be email'able as one file, even if I install it with pip and pip needs stuff I'd like it to be just one file in the src
- [x] 'do one thing well', just type check, no formatting
    - I think I want to remove formatting with black and isort, I find when I'm working on something I want to type check every single time I run, but I only really want to format once at the end before committing.
        - I've actually had times where isort has broken my programs, when I'm type checking I don't want my programs to break
- [x] Install with pip, as a command line command
    - There's currently four steps in the install process, that's 3 too many.
    - I've never done this, but my understanding is it has to do with `entry_points`, see (this could be wrong, but asking online I was told it has something to do with `entry_points`):
        - NEW THING: https://packaging.python.org/en/latest/specifications/entry-points/
        - OLD THING: https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html
    - One main issue is how do you `brew install coreutils` on macos? Worst case I could issue a runtime warning, as I do for the `py` command with instructions
- [ ] I should figure out a way to use pytest for this
- [x] What's the default type checker?
    - mypy
        - I really don't like having to add `ignore_missing_imports` everytime I use mypy, I really want to make it the default like with the `--pretty`. On the other hand, maybe I should remove all default opinions so `mypy` behaves how `mypy` behaves
    - pyright
        - has the problem that the fast version is `npm`, which I don't know how to install with pip. the pip pyright version is very slow to startup and I can't figure out how to make it not check for updates.
        - has a lot of noise in the output
    - pytype
        - doesn't support 3.10, which means as a default it's probably not the best because people (me) will want to use up to date python versions
- [x] I need 3.11 for the built in toml parsing, although I guess if I'm installing with pip a python dependency is fine. It's slightly unfortunate
- [ ] Add `-h/--help` logic
- [ ] Add `-q` logic
