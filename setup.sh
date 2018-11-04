#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

[[ -d ${DIR}/venv ]] && rm -rf ${DIR}/venv
virtualenv -p python3 ${DIR}/venv
source ${DIR}/venv/bin/activate

pip install -r ${DIR}/requirements.txt
pip install -e ${DIR}