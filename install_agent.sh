#!/bin/bash

# Update package lists
sudo apt-get update

# Install necessary packages (example for a Linux system)
sudo apt-get install -y python3 python3-pip snort

# Install and configure Wazuh agent (example)
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | sudo apt-key add -
echo "deb https://packages.wazuh.com/4.x/apt/ stable main" | sudo tee -a /etc/apt/sources.list.d/wazuh.list
sudo apt-get update
sudo apt-get install -y wazuh-agent

# Configure the agent to communicate with the Wazuh manager
sudo sed -i 's/MANAGER_IP/your_wazuh_manager_ip/' /var/ossec/etc/ossec.conf

# Enable and start the Wazuh agent
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
