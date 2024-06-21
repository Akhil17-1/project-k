# Project K

## Overview
Project K is designed to collect, process, and store logs from various sources into a MongoDB database. The project includes scripts for collecting logs from Windows Event Viewer and other sources, processing them, and storing them efficiently.

## Features
- Collection of logs from Windows Event Viewer
- Segregation of logs into various categories for better organization
- Storage of logs in MongoDB
- Handling large logs by splitting them into manageable chunks
- Automated script to start MongoDB, log collector, and agent simultaneously

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Akhil17-1/project-k.git
   cd project-k
Install dependencies:

bash
Copy code
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
Start MongoDB, log collector, and agent:

bash
Copy code
.\start_all.bat
Usage
Collect logs using the agent:

bash
Copy code
python agent.py
Start the log collector:

bash
Copy code
python log_collector.py
Log Types
The following log types are collected and stored in MongoDB under Project K:

Application
System
Security
Setup
Forwarded Events
CustomApplication
Network
Application Firewall
Issues and Challenges
Please refer to the challenges.md file for a detailed description of the issues faced and the solutions implemented.

License
MIT

css
Copy code

### Updated Checklist_of_Objectives.md

```markdown
# Checklist of Objectives

## Completed
- [x] Setup MongoDB for log storage
- [x] Develop agent.py for collecting logs from Windows Event Viewer
- [x] Implement log_collector.py for processing and storing logs
- [x] Create a script to start MongoDB, log collector, and agent simultaneously
- [x] Segregate logs into categories for better organization
- [x] Handle large log files by splitting them into chunks
- [x] Limit log file size to 100 MB and delete the earliest logs when full

## In Progress
- [ ] Optimize log collection process
- [ ] Implement additional log sources (e.g., IIS, PowerShell)

## To Do
- [ ] Enhance log searching and filtering capabilities
- [ ] Improve error handling and logging within scripts
- [ ] Add support for remote log collection