from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Configure MongoDB client with SSL disabled
client = MongoClient('mongodb://localhost:27017/', tlsAllowInvalidCertificates=True)
db = client['project_k']

@app.route('/')
def home():
    return "Welcome to Project K!"

@app.route('/collect-log', methods=['POST'])
def collect_log():
    log_data = request.json
    db.logs.insert_one(log_data)
    return jsonify({"message": "Log collected"}), 200

if __name__ == '__main__':
    app.run(debug=True)
