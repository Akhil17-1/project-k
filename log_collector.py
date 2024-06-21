from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import logging
import re

app = Flask(__name__)
CORS(app)

# Setup logging
logging.basicConfig(level=logging.DEBUG, filename='log_collector.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['project_k']

def sanitize_collection_name(name):
    """Sanitize the collection name to be MongoDB-compatible."""
    return re.sub(r'\.', '_', name)

@app.route('/collect-log', methods=['POST'])
def collect_log():
    logs = request.json
    log_type = logs.get('source', 'Unknown')  # Use the 'source' as log type
    if log_type == "Combined Logs":
        for log in logs['logs']:
            log_type = sanitize_collection_name(log.get('SourceName', 'Unknown'))
            collection = db[log_type]
            try:
                collection.insert_one(log)
                logging.info(f"Successfully received log for {log_type}")
            except Exception as e:
                logging.error(f"Error saving log to MongoDB: {e}")
                return jsonify({"error": str(e)}), 500
    return jsonify({"message": f"Successfully received {len(logs['logs'])} logs"}), 200

@app.route('/logs/<log_type>', methods=['GET'])
def get_logs(log_type):
    log_type = sanitize_collection_name(log_type)
    logs = list(db[log_type].find())
    for log in logs:
        log['_id'] = str(log['_id'])
    return jsonify(logs), 200

@app.route('/status', methods=['GET'])
def get_status():
    status = {}
    log_types = [
        'Application', 'System', 'Security', 'Setup', 'ForwardedEvents',
        'CustomApplication', 'Network', 'Application Firewall'
    ]
    for log_type in log_types:
        status[log_type] = db.status.find_one().get(log_type, 'Not found')
    return jsonify(status), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
