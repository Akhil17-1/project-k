@echo off

REM Set up virtual environment if not already set
IF NOT EXIST "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate the virtual environment
call venv\Scripts\activate

REM Install necessary dependencies
echo Installing dependencies...
pip install -r requirements.txt
pip install pytest pytest-mock

REM Set the PYTHONPATH to the project root
set PYTHONPATH=%CD%

REM Run the tests
echo Running tests...
pytest

REM Deactivate the virtual environment
deactivate

echo Tests completed.
pause
