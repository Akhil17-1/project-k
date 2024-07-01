from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import logging

app = Flask(__name__)
CORS(app)

# MongoDB Client
client = MongoClient('mongodb://localhost:27017/')
db = client['project_k']

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    return "Welcome to the log collector app!", 200

@app.route('/collect-log', methods=['POST'])
def collect_log():
    data = request.json
    if 'logs' not in data or not isinstance(data['logs'], list):
        return jsonify({"error": "Invalid log data"}), 400

    collection_name = data.get('source', 'Combined Logs')
    collection = db[collection_name]
    
    if data['logs']:
        collection.insert_many(data['logs'])
    else:
        logging.error("No logs to insert")
    
    return jsonify({"status": "Logs collected successfully"}), 200

@app.route('/logs/<log_type>', methods=['GET'])
def get_logs(log_type):
    log_type_map = {
        "Application": "Combined Logs",
        "System": "Combined Logs",
        "Security": "Combined Logs",
        "Network": "Combined Logs",
        "Firewall": "Combined Logs",
        "Install": "Combined Logs",
        "User": "Combined Logs"
    }

    collection_name = log_type_map.get(log_type, None)
    if not collection_name or collection_name not in db.list_collection_names():
        logging.debug(f"Log type {log_type} not found in collections.")
        return jsonify({"error": "Log type not found"}), 404

    logs = list(db[collection_name].find({"SourceName": {"$regex": log_type}}))
    logging.debug(f"Fetched {len(logs)} logs for log type {log_type}.")
    for log in logs:
        log['_id'] = str(log['_id'])
    return jsonify(logs), 200

@app.route('/status', methods=['GET'])
def get_status():
    status = {}
    log_types = db.list_collection_names()
    total_logs = 0
    error_logs = 0
    last_log_collected = None

    for log_type in log_types:
        count = db[log_type].count_documents({})
        if count > 0:
            last_log = db[log_type].find().sort('timestamp', -1).limit(1)[0]
            if 'timestamp' in last_log:
                last_log_collected = last_log['timestamp'] if not last_log_collected else max(last_log_collected, last_log['timestamp'])
            total_logs += count
        status[log_type] = {
            'count': count,
            'lastCollected': last_log['timestamp'] if count > 0 and 'timestamp' in last_log else None
        }

    if total_logs > 0:
        success_percentage = ((total_logs - error_logs) / total_logs) * 100
    else:
        success_percentage = 0

    status['totalLogs'] = total_logs
    status['lastLogCollected'] = last_log_collected
    status['errorLogs'] = error_logs
    status['successPercentage'] = success_percentage

    return jsonify(status), 200

if __name__ == '__main__':
    app.run(debug=True)
