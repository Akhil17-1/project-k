
# Project K

A cybersecurity application for log collection, vulnerability assessment, and threat detection.

## Project Overview

Project K is designed to collect logs from various sources, including Windows Event Viewer, network logs, application firewall logs, user logs, and installation logs. These logs are aggregated and stored in MongoDB for further analysis and visualization.

## Features

- Collects logs from Windows Event Viewer (Application, System, Security, User, Install logs).
- Collects logs from specified log files (Network, Application Firewall).
- Aggregates logs and stores them in MongoDB.
- Provides real-time log collection status updates every 30 seconds.

## Setup Instructions

### Prerequisites

- Python 3.x
- MongoDB
- Flask
- MongoDB Compass (optional, for viewing logs)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/project-k.git
   cd project-k
   ```

2. **Set up a virtual environment:**
   ```sh
   python3 -m venv venv
   venv\Scripts\activate  # For Windows
   ```

3. **Install required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure MongoDB:**
   - Ensure MongoDB is running on `localhost:27017`.

### Running the Application

1. **Start the Flask server:**
   ```sh
   cd project-k
   venv\Scripts\activate  # Activate the virtual environment if not already activated
   python app.py
   ```

2. **Run the agent script:**
   ```sh
   cd agent
   venv\Scripts\activate  # Activate the virtual environment if not already activated
   python agent.py
   ```

### Viewing Logs

- Use MongoDB Compass to connect to the MongoDB instance and navigate to the `project_k` database.
- Open the `logs` collection to view the aggregated logs.

## Today's Update (2024-06-20)

### New Features and Updates:

- **Log Collection Enhancement:** 
  - The agent script has been updated to collect logs from multiple sources, including Windows Event Viewer (Application, System, Security, User, Install logs) and specified log files (Network, Application Firewall).
  - The agent script now updates the log collection status every 30 seconds, indicating which logs have been collected and which have not been found.

### Implementation Details:

- **Windows Event Viewer Logs:** 
  - The agent script collects logs from the Application, System, Security, User, and Install logs using the `win32evtlog` module.
  - Necessary privileges are set to allow the script to read the Event Logs.

- **Log File Collection:**
  - The agent script collects logs from specified network and application firewall log files.
  - Paths to these log files can be configured in the script.

- **Status Updates:**
  - The agent script provides real-time updates on the log collection status every 30 seconds.
  - The status includes information on whether logs were collected or not found for each log type.

### Example Output:

- **Flask Server Output:**
  - Displays messages indicating successful receipt and processing of logs.

- **Agent Script Output:**
  - Provides real-time status updates on the log collection process.
  - Logs sent successfully: `[INFO] Logs sent successfully`

- **MongoDB Compass:**
  - Aggregated logs can be viewed in the `logs` collection within the `project_k` database.

## Contribution

Feel free to contribute to the project by submitting pull requests, reporting issues, or suggesting new features.

## License

This project is licensed under the MIT License.
```

This updated `README.md` file provides clear instructions on setting up and running the application, along with details about the recent updates and features added today. If you have any further changes or additions, let me know!
