import os
import time
import json
import logging
import requests
from pymongo import MongoClient

SERVER_URL = 'http://localhost:5000/collect-log'
LOG_FILE_PATHS = {
    "Network": "C:\\Logs\\network.log",
    "Application Firewall": "C:\\Logs\\firewall.log",
}
POLL_INTERVAL = 1800  # 30 minutes in seconds

# MongoDB Client
client = MongoClient('mongodb://localhost:27017/')
db = client['project_k']

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def collect_file_logs(file_path):
    if not os.path.exists(file_path):
        logging.error(f"Log file not found: {file_path}")
        return []

    with open(file_path, "r") as file:
        logs = file.readlines()
    
    file_logs = []
    for log in logs:
        file_logs.append({
            "log": log.strip(),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        })
    
    return file_logs

def send_logs(log_data):
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(SERVER_URL, headers=headers, data=json.dumps(log_data))
        if response.status_code == 200:
            logging.info("Logs sent successfully")
        else:
            logging.error(f"Failed to send logs: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error sending logs: {e}")

def update_status(status):
    logging.info("Dropping status collection")
    db.status.drop()
    logging.info("Inserting new status")
    db.status.insert_one(status)
    logging.info("Status updated")

def main():
    while True:
        all_logs = []
        status = {}

        # Collect file logs
        for log_type, file_path in LOG_FILE_PATHS.items():
            logs_collected = collect_file_logs(file_path)
            if logs_collected:
                all_logs.extend(logs_collected)
                status[log_type] = "Collected"
            else:
                status[log_type] = "Not found"

        if all_logs:
            log_data = {
                "source": "Combined Logs",
                "logs": all_logs,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            }
            send_logs(log_data)
        
        update_status(status)
        logging.info(f"Log collection status: {status}")
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()
