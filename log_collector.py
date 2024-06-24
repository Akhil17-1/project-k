import os
import time
import logging
import requests
import json
import win32evtlog
import win32security
import win32api
from pymongo import MongoClient

# Configuration
SERVER_URL = "http://localhost:5000/collect-log"
EVENT_LOG_SOURCES = {
    "Application": ["Application", "Application Error", "DellTechHub", "Desktop Window Manager", "FusionService", "MsiInstaller", "SDSSnapshotProcess"],
    "System": ["System", "Microsoft-Windows-CAPI2", "Microsoft-Windows-Defrag", "Microsoft-Windows-RestartManager", "Software Protection Platform Service", "VSS", "Windows Error Reporting", "Wlclntfy", "edgeupdate"],
    "Security": ["Security", "SecurityCenter"],
    "Setup": ["Setup"],
    "ForwardedEvents": ["ForwardedEvents"],
    "CustomApplication": ["Alienware SupportAssist Remediation", "logs", "status"],
}
LOG_FILE_PATHS = {
    "Network": "C:\\Logs\\network.log",
    "Application Firewall": "C:\\Logs\\firewall.log",
}
POLL_INTERVAL = 1800  # 30 minutes in seconds

# MongoDB Client
client = MongoClient('mongodb://localhost:27017/')
db = client['project_k']

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

EVENT_TYPE_MAPPING = {
    win32evtlog.EVENTLOG_AUDIT_FAILURE: "Audit Failure",
    win32evtlog.EVENTLOG_AUDIT_SUCCESS: "Audit Success",
    win32evtlog.EVENTLOG_INFORMATION_TYPE: "Information",
    win32evtlog.EVENTLOG_WARNING_TYPE: "Warning",
    win32evtlog.EVENTLOG_ERROR_TYPE: "Error",
}

def set_privilege(privilege_name, enable=True):
    """Set or remove a privilege for the current process."""
    flags = win32security.TOKEN_ADJUST_PRIVILEGES | win32security.TOKEN_QUERY
    hToken = win32security.OpenProcessToken(win32api.GetCurrentProcess(), flags)
    privilege_id = win32security.LookupPrivilegeValue(None, privilege_name)
    if enable:
        new_privilege = [(privilege_id, win32security.SE_PRIVILEGE_ENABLED)]
    else:
        new_privilege = [(privilege_id, 0)]
    win32security.AdjustTokenPrivileges(hToken, False, new_privilege)
    win32api.CloseHandle(hToken)

def collect_event_logs(source):
    logs = []
    try:
        set_privilege(win32security.SE_SECURITY_NAME, True)  # Enable necessary privilege
        log_handle = win32evtlog.OpenEventLog(None, source)
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        total = win32evtlog.GetNumberOfEventLogRecords(log_handle)
        while True:
            events = win32evtlog.ReadEventLog(log_handle, flags, 0)
            if not events:
                break
            for event in events:
                log_entry = {
                    "EventCategory": event.EventCategory,
                    "TimeGenerated": str(event.TimeGenerated),
                    "SourceName": event.SourceName,
                    "EventID": event.EventID,
                    "EventType": event.EventType,
                    "EventTypeName": EVENT_TYPE_MAPPING.get(event.EventType, "Unknown"),
                    "Message": event.StringInserts
                }
                logs.append(log_entry)
            if len(logs) >= total:
                break
    except Exception as e:
        logging.error(f"Error collecting event logs from {source}: {e}")
    finally:
        set_privilege(win32security.SE_SECURITY_NAME, False)  # Disable the privilege after use
    return logs

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
    db.status.drop()
    db.status.insert_one(status)

def main():
    while True:
        all_logs = []
        status = {}

        # Collect event logs
        for log_type, sources in EVENT_LOG_SOURCES.items():
            logs_collected = []
            for source in sources:
                logs_collected.extend(collect_event_logs(source))
            if logs_collected:
                all_logs.extend(logs_collected)
                status[log_type] = "Collected"
            else:
                status[log_type] = "Not found"

        # Collect file logs
        for log_type, file_path in LOG_FILE_PATHS.items():
            logs_collected = collect_file_logs(file_path)
            if logs_collected:
                all_logs.extend(logs_collected)
                status[log_type] = "Collected"
            else:
                status[log_type] = "Not found"

        if all_logs:
            chunk_size = 16 * 1024 * 1024  # 16 MB chunk size to avoid BSON size limit
            for i in range(0, len(all_logs), chunk_size):
                chunk = all_logs[i:i + chunk_size]
                log_data = {
                    "source": "Combined Logs",
                    "logs": chunk,
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
                }
                send_logs(log_data)
        
        update_status(status)
        logging.info(f"Log collection status: {status}")
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()
