from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['logs_db']

@app.route('/logs/<log_type>', methods=['GET'])
def get_logs(log_type):
    logs = list(db[log_type].find())
    for log in logs:
        log['_id'] = str(log['_id'])
    return jsonify(logs), 200

@app.route('/status', methods=['GET'])
def get_status():
    status = {}
    log_types = ['Application', 'System', 'Security', 'Setup', 'ForwardedEvents', 'Network', 'Firewall']
    for log_type in log_types:
        count = db[log_type].count_documents({})
        status[log_type] = 'Collected' if count > 0 else 'Not found'
    return jsonify(status), 200

if __name__ == '__main__':
    app.run(debug=True)
