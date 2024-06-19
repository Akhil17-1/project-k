import os
import platform
import subprocess

def install_packages():
    if platform.system() == "Windows":
        subprocess.run(["powershell", "-Command", "choco install python3 snort -y"], check=True)
    elif platform.system() == "Linux":
        subprocess.run(["sudo", "apt-get", "update"], check=True)
        subprocess.run(["sudo", "apt-get", "install", "-y", "python3", "python3-pip", "snort"], check=True)
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(["brew", "install", "python", "snort"], check=True)
    else:
        print("Unsupported OS")

def configure_agent(manager_ip):
    if platform.system() == "Windows":
        subprocess.run(["powershell", "-Command", "(Get-Content -Path 'C:\\Program Files\\ossec-agent\\ossec.conf') -replace 'MANAGER_IP', '{0}' | Set-Content -Path 'C:\\Program Files\\ossec-agent\\ossec.conf'".format(manager_ip)], check=True)
    elif platform.system() == "Linux":
        subprocess.run(["sudo", "sed", "-i", "s/MANAGER_IP/{}/".format(manager_ip), "/var/ossec/etc/ossec.conf"], check=True)
    else:
        print("Unsupported OS")

def start_agent():
    if platform.system() == "Windows":
        subprocess.run(["net", "start", "WazuhAgent"], check=True)
    elif platform.system() == "Linux":
        subprocess.run(["sudo", "systemctl", "enable", "wazuh-agent"], check=True)
        subprocess.run(["sudo", "systemctl", "start", "wazuh-agent"], check=True)
    else:
        print("Unsupported OS")

def main():
    manager_ip = input("Enter the IP address of the Wazuh manager: ")
    install_packages()
    configure_agent(manager_ip)
    start_agent()
    print("Agent installation and configuration complete.")

if __name__ == "__main__":
    main()

