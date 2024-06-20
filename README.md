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
   git clone https://github.com/akhil17-1/project-k.git
   cd project-k
