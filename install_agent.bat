@echo off

REM Update package lists
echo Updating package lists...
powershell -Command "Start-Process 'powershell.exe' -ArgumentList 'choco upgrade chocolatey' -Verb RunAs"
powershell -Command "Start-Process 'powershell.exe' -ArgumentList 'choco upgrade all' -Verb RunAs"

REM Install necessary packages (example for a Windows system)
echo Installing necessary packages...
powershell -Command "Start-Process 'powershell.exe' -ArgumentList 'choco install python3' -Verb RunAs"
powershell -Command "Start-Process 'powershell.exe' -ArgumentList 'choco install snort' -Verb RunAs"

REM Install and configure Wazuh agent (example)
echo Installing Wazuh agent...
powershell -Command "Invoke-WebRequest -Uri 'https://packages.wazuh.com/4.x/windows/wazuh-agent-4.2.5-1.msi' -OutFile 'wazuh-agent.msi'"
msiexec /i wazuh-agent.msi /quiet

REM Configure the agent to communicate with the Wazuh manager
echo Configuring Wazuh agent...
powershell -Command "(Get-Content -Path 'C:\\Program Files (x86)\\ossec-agent\\ossec.conf') -replace 'MANAGER_IP', 'your_wazuh_manager_ip' | Set-Content -Path 'C:\\Program Files (x86)\\ossec-agent\\ossec.conf'"

REM Enable and start the Wazuh agent
echo Enabling and starting Wazuh agent...
sc config WazuhAgent start= auto
net start WazuhAgent

echo Installation and configuration complete.
pause

