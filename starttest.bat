@echo off

REM Start all services and applications
echo Starting all services and applications...
start /b call start_all.bat

REM Wait a bit to ensure services are up
echo Waiting for services to start...
timeout /t 30 /nobreak > NUL

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
pytest --junitxml=results.xml

REM Deactivate the virtual environment
deactivate

REM Provide feedback on test results
echo Test results:
type results.xml

pause
