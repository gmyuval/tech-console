#!/usr/bin/env bash
export PYTHON_BIN_PATH="$(python3 -m site --user-base)/bin"
export PATH="$PATH:$PYTHON_BIN_PATH"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

[[ -d ${DIR}/venv ]] && rm -rf ${DIR}/venv
cd ${DIR}
pip install pipenv

pipenv install --dev