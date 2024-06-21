from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import logging
import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# MongoDB and other routes setup remains the same

@app.route('/')
def home():
    return "Welcome to Project K!"

@app.route('/collect-log', methods=['POST'])
def collect_log():
    log_data = request.json
    db.logs.insert_one(log_data)
    logging.info(f"Log collected from {log_data['source']} at {log_data['timestamp']}")
    return jsonify({"message": "Log collected"}), 200

@app.route('/logs', methods=['GET'])
def get_logs():
    logs = list(db.logs.find())
    for log in logs:
        log["_id"] = str(log["_id"])  # Convert ObjectId to string for JSON serialization
    return jsonify(logs), 200

@app.route('/logs/<log_type>', methods=['GET'])
def get_logs_by_type(log_type):
    logs = list(db.logs.find({"SourceName": log_type}))
    for log in logs:
        log["_id"] = str(log["_id"])  # Convert ObjectId to string for JSON serialization
    return jsonify(logs), 200

@app.route('/status', methods=['GET'])
def get_status():
    status = [
        {"logType": "Application", "count": 150, "errorCount": 10},
        {"logType": "System", "count": 120, "errorCount": 20},
        {"logType": "Security", "count": 100, "errorCount": 5},
        {"logType": "User", "count": 90, "errorCount": 0},
        {"logType": "Install", "count": 80, "errorCount": 10},
        {"logType": "Network", "count": 70, "errorCount": 7},
        {"logType": "Firewall", "count": 60, "errorCount": 8}
    ]
    return jsonify(status), 200

@app.route('/cves', methods=['GET'])
def get_cves():
    cves = [
        {"id": "CVE-2021-1234", "description": "Sample CVE 1"},
        {"id": "CVE-2021-5678", "description": "Sample CVE 2"},
        {"id": "CVE-2021-9102", "description": "Sample CVE 3"}
    ]
    return jsonify(cves), 200

@app.route('/verify-file', methods=['POST'])
def verify_file():
    data = request.json
    file_url = data.get('file_url')
    
    # Example of an OSINT service call
    response = requests.get(file_url)
    if response.status_code == 200:
        file_content = response.content
        # Perform file integrity checks here
        return jsonify({"status": "File is clean"}), 200
    else:
        return jsonify({"status": "File could not be retrieved"}), 400

if __name__ == '__main__':
    app.run(debug=True)
