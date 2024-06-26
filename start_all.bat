@echo off

echo Starting MongoDB service...
net start MongoDB

rem Wait for MongoDB to start
timeout /t 5 /nobreak > NUL

echo Starting Flask app...
start "Flask App" cmd /k "call venv\Scripts\activate && python C:\Users\Akhil\project-k\app.py"

rem Wait for Flask app to start
timeout /t 5 /nobreak > NUL

echo Starting log_collector.py...
start "Log Collector" cmd /k "call venv\Scripts\activate && python C:\Users\Akhil\project-k\log_collector.py"

rem Wait for log_collector.py to start
timeout /t 5 /nobreak > NUL

echo Starting agent.py...
start "Agent" cmd /k "call venv\Scripts\activate && python C:\Users\Akhil\project-k\agent.py"

rem Wait for agent.py to start
timeout /t 5 /nobreak > NUL

echo Starting frontend...
start "Frontend" cmd /k "cd C:\Users\Akhil\project-k\frontend && npm start"

rem Wait for frontend to start
timeout /t 5 /nobreak > NUL

echo All services started. Press Ctrl+C to stop.

rem Keep the script running
:loop
timeout /t 1 /nobreak > NUL
goto loop

rem Cleanup when script is stopped
:cleanup
echo Stopping all services...
net stop MongoDB
taskkill /f /im python.exe
taskkill /f /im node.exe
exit
