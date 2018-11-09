#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

[[ -d ${DIR}/venv ]] && rm -rf ${DIR}/venv
cd ${DIR}
pip install pipenv

pipenv install --dev