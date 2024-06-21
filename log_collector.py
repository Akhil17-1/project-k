import logging
from logging.handlers import RotatingFileHandler
import time
from flask import Flask, request
from pymongo import MongoClient, errors

# Configuration
LOG_FILE_PATH = 'Nlog_collector.log'  # Updated log file name
MAX_LOG_SIZE = 100 * 1024 * 1024  # 100 MB
BACKUP_COUNT = 5
MAX_BSON_SIZE = 16 * 1024 * 1024  # 16 MB
MAX_CHUNK_SIZE = MAX_BSON_SIZE - 1024 * 1024  # Further reduced buffer to handle BSON overhead

# Set up logging
handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[handler])

app = Flask(__name__)

# MongoDB Client
client = MongoClient('mongodb://localhost:27017/')
db = client['project_k']

def split_logs(log_data, max_size=MAX_CHUNK_SIZE):
    chunks = []
    current_chunk = []
    current_size = 0

    for log in log_data:
        log_size = len(str(log).encode('utf-8'))
        
        # If adding this log exceeds max size, start a new chunk
        if current_size + log_size > max_size:
            chunks.append(current_chunk)
            current_chunk = [log]
            current_size = log_size
        else:
            current_chunk.append(log)
            current_size += log_size
    
    # Add the last chunk if not empty
    if current_chunk:
        chunks.append(current_chunk)

    return chunks

@app.route('/collect-log', methods=['POST'])
def collect_log():
    logging.info("Received request to /collect-log endpoint")
    data = request.get_json()
    log_type = data.get('source')
    log_data = data.get('logs')

    if log_type and log_data:
        logging.info(f"Processing logs for type: {log_type}")
        chunks = split_logs(log_data)
        collection = db[log_type]
        for chunk in chunks:
            try:
                # Log chunk size for debugging
                chunk_size = len(str(chunk).encode('utf-8'))
                logging.info(f"Inserting chunk of size {chunk_size} bytes")
                
                collection.insert_one({
                    'log_data': chunk,
                    'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
                })
                logging.info(f'Successfully inserted logs for {log_type}')
            except errors.DocumentTooLarge as e:
                logging.error(f"Failed to insert logs for {log_type}: {e}")
        return 'Logs received', 200
    else:
        logging.error('Invalid log data received')
        return 'Invalid data', 400

if __name__ == '__main__':
    logging.info("Starting log collector service")
    app.run(port=5000, debug=True)
