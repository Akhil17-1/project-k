from flask import Flask, request, jsonify
from pymongo import MongoClient
import logging

app = Flask(__name__)

# Configure MongoDB client without ssl_cert_reqs
client = MongoClient('mongodb://localhost:27017/')
db = client['project_k']

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    return "Welcome to Project K!"

@app.route('/collect-log', methods=['POST'])
def collect_log():
    log_data = request.json
    # Perform basic processing
    log_data['processed'] = True
    db.logs.insert_one(log_data)
    logging.info(f"Log collected from {log_data['source']} at {log_data['timestamp']}")
    return jsonify({"message": "Log collected"}), 200

if __name__ == '__main__':
    app.run(debug=True)
