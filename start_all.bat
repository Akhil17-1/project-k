@echo off
echo Starting MongoDB service...
net start MongoDB

rem Wait for MongoDB to start
timeout /t 5 /nobreak > NUL

echo Starting log_collector.py...
start "Log Collector" cmd /c "python log_collector.py"

rem Wait for log_collector.py to start
timeout /t 5 /nobreak > NUL

echo Starting agent.py...
start "Agent" cmd /c "python agent.py"

rem Wait for agent.py to start
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
exit
