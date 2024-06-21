def collect_and_save_logs():
    log_types = ['Application', 'System', 'Security', 'Setup', 'ForwardedEvents']
    for log_type in log_types:
        logs = collect_event_logs(log_type)
        save_logs_to_mongodb(logs, log_type)
        rotate_logs(log_type)

def rotate_logs(log_type):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs_db']
    collection = db[log_type]
    max_logs = 10000  # Set a maximum limit for logs
    if collection.count_documents({}) > max_logs:
        to_delete = collection.find().sort('timestamp', 1).limit(collection.count_documents({}) - max_logs)
        for doc in to_delete:
            collection.delete_one({'_id': doc['_id']})
