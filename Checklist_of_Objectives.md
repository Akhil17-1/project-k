Objective 1: Endpoint Development
 Create an Agent from scratch
Developed a Python agent script to collect logs from Windows Event Viewer and specified log files.
Set up MongoDB to store collected logs.
Ensured the agent sends logs to a central server.
Handled log file size limits and document size limits in MongoDB.
Objective 2: Central Server
 Develop the Central Server
Created a Flask server to receive logs from the agent.
Stored logs in MongoDB.
Added endpoints to fetch logs and log status from MongoDB.
Implemented CORS support to allow frontend access.
Improved error handling for large logs and splitting logs into chunks.
Objective 3: Frontend Development
 Setup Frontend with React and Visual Studio Code

Created a React frontend using create-react-app.
Installed necessary dependencies (Axios, React Router, react-chartjs-2, and Chart.js).
 Home Screen Development

Designed a Netflix-style home screen with options to navigate to different log types.
Displayed log success/error ratios.
Applied dynamic themes based on the log success rate.
Displayed top CVEs in a dynamic pattern.
 Log Type Screens

Developed components to display logs based on selected log types.
Displayed logs systematically in a list format.
Integrated a chart to visually represent log counts.
Objective 4: Security and Additional Features
 Implement Built-in Antivirus and Strong Vault for Password Security

Pending: Integrate antivirus solutions.
Pending: Implement a secure vault for password management.
 XDR, EDR Approach

Pending: Define and implement an Extended Detection and Response (XDR) and Endpoint Detection and Response (EDR) approach.
Objective 5: Final Integration and Testing
 Local Testing
Ensure all components work seamlessly together locally.
Conduct thorough testing to verify data collection, storage, and display functionalities.
Updated Task Breakdown
Endpoint Development

 Develop and test the agent script.
 Ensure logs are collected from Windows Event Viewer and specified log files.
 Send collected logs to the central server.
 Handle log file size limits and MongoDB document size limits.
Central Server

 Set up Flask server with necessary endpoints.
 Store logs in MongoDB.
 Implement CORS support.
 Improve error handling for large logs and splitting logs into chunks.
Frontend Development

 Create the React app and set up the project structure.
 Develop the home screen with dynamic themes and top CVEs display.
 Create log type screens to display logs based on selected types.
 Integrate charts to visualize log data.
Security and Additional Features

 Integrate antivirus solutions.
 Implement a secure vault for password management.
 Define and implement XDR and EDR approaches.
Integration and Testing

 Ensure all components work seamlessly together.
 Conduct thorough testing to verify data collection, storage, and display functionalities.
Challenges and Issues
Issue 1: Large Log File Size
Problem: The log_collector.log file exceeded GitHub's file size limit of 100 MB, causing push errors.
Solution: Implemented a mechanism to limit the log file size to 100 MB by splitting logs into chunks and deleting the oldest logs when the limit is reached.
Issue 2: BSON Document Size Limit
Problem: BSON document size exceeded MongoDB's limit of 16 MB, causing insertion errors.
Solution: Modified the log_collector.py script to split large log documents into smaller chunks before inserting them into MongoDB.
Issue 3: Log File Not Found
Problem: Certain log files (e.g., network.log, firewall.log) were not found, causing errors in agent.py.
Solution: Added error handling to skip missing log files and continue processing.
Issue 4: Git Repository Cleanup
Problem: Needed to remove large files from the Git repository to comply with GitHub's size limits.
Solution: Used BFG Repo-Cleaner to strip large files from the repository history and cleaned up with git reflog and git gc.
Ongoing Challenges
Optimization: Continuously optimizing the log collection and processing scripts for better performance and reliability.
Error Handling: Improving error handling within scripts to ensure robustness and stability.
Documentation: Keeping documentation up-to-date with ongoing developments and changes.
This checklist should help guide the remaining tasks and ensure we stay on track with the project development. If you need further adjustments or additions, please let me know!