#!/usr/bin/env bash
set -eou pipefail
rm -rf dist
py -m pip install --upgrade build
py -m build
py -m pip install --upgrade twine
py -m twine upload dist/*
printf "python3 -m pip install ty-command\n"
