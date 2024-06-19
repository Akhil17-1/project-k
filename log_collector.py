import requests

log_entry = {
    "source": "server1",
    "log": "Failed login attempt",
    "timestamp": "2024-06-19T12:34:56Z"
}

response = requests.post('http://localhost:5000/collect-log', json=log_entry)
print(response.json())
