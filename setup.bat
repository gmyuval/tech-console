set drive=%~d0
set scriptpath=%~dp0
pip install pipenv
%~d0
cd %~dp0
pipenv install --dev