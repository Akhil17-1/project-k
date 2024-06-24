from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import time

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['project_k']

@app.route('/logs/<log_type>', methods=['GET'])
def get_logs(log_type):
    if log_type not in db.list_collection_names():
        return jsonify({"error": "Log type not found"}), 404

    logs = list(db[log_type].find())
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
