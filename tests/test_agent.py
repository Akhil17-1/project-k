import pytest
from agent import collect_event_logs, collect_file_logs, send_logs, update_status
from unittest.mock import patch, mock_open

@patch('agent.requests.post')
def test_send_logs_success(mock_post):
    """Test sending logs successfully."""
    mock_post.return_value.status_code = 200
    log_data = {"source": "Test Logs", "logs": [], "timestamp": "2024-06-24T16:00:00Z"}
    send_logs(log_data)
    mock_post.assert_called_once()

@patch('agent.requests.post')
def test_send_logs_failure(mock_post):
    """Test sending logs failure."""
    mock_post.return_value.status_code = 500
    log_data = {"source": "Test Logs", "logs": [], "timestamp": "2024-06-24T16:00:00Z"}
    send_logs(log_data)
    mock_post.assert_called_once()

@patch('agent.win32evtlog.OpenEventLog', return_value=None)
def test_collect_event_logs(mock_open_event_log):
    """Test collecting event logs."""
    logs = collect_event_logs("Application")
    assert isinstance(logs, list)

@patch('builtins.open', new_callable=mock_open, read_data="test log")
@patch('agent.os.path.exists', return_value=True)
def test_collect_file_logs(mock_exists, mock_file):
    """Test collecting file logs."""
    logs = collect_file_logs("test.log")
    assert isinstance(logs, list)
    assert len(logs) > 0

def test_update_status(mocker):
    """Test updating status."""
    mock_drop = mocker.patch('agent.db.status.drop')
    mock_insert = mocker.patch('agent.db.status.insert_one')
    status = {"Application": "Collected"}
    update_status(status)
    mock_drop.assert_called_once()
    mock_insert.assert_called_once_with(status)
