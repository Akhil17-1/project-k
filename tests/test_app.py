import pytest
import json
from app import app, client

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home page."""
    rv = client.get('/')
    assert rv.status_code == 200

def test_get_logs(client):
    """Test getting logs of a specific type."""
    rv = client.get('/logs/Application')
    assert rv.status_code in [200, 404]

def test_get_status(client):
    """Test getting the status."""
    rv = client.get('/status')
    assert rv.status_code == 200
    data = rv.get_json()
    assert 'totalLogs' in data
    assert 'lastLogCollected' in data
    assert 'errorLogs' in data
    assert 'successPercentage' in data

def test_collect_log(client, mocker):
    """Test the collect log endpoint."""
    mocker.patch('app.db.collection.insert_many', return_value=None)
    log_data = {
        "source": "Test Logs",
        "logs": [],
        "timestamp": "2024-06-24T16:00:00Z"
    }
    rv = client.post('/collect-log', data=json.dumps(log_data), content_type='application/json')
    assert rv.status_code == 200
