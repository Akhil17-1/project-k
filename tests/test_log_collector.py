import pytest
from log_collector import collect_file_logs, send_logs, update_status
from unittest.mock import patch, mock_open

@patch('log_collector.requests.post')
def test_send_logs_success(mock_post):
    """Test sending logs successfully."""
    mock_post.return_value.status_code = 200
    log_data = {"source": "Test Logs", "logs": [{"event": "test log"}], "timestamp": "2024-06-24T16:00:00Z"}
    send_logs(log_data)
    mock_post.assert_called_once()

@patch('log_collector.requests.post')
def test_send_logs_failure(mock_post):
    """Test sending logs failure."""
    mock_post.return_value.status_code = 500
    log_data = {"source": "Test Logs", "logs": [{"event": "test log"}], "timestamp": "2024-06-24T16:00:00Z"}
    send_logs(log_data)
    mock_post.assert_called_once()

@patch('builtins.open', new_callable=mock_open, read_data="test log")
@patch('log_collector.os.path.exists', return_value=True)
def test_collect_file_logs(mock_exists, mock_file):
    """Test collecting file logs."""
    logs = collect_file_logs("test.log")
    assert isinstance(logs, list)
    assert len(logs) > 0

def test_update_status(mocker):
    """Test updating status."""
    mock_drop = mocker.patch('log_collector.db.status.drop')
    mock_insert = mocker.patch('log_collector.db.status.insert_one')
    status = {"Application": "Collected"}
    update_status(status)
    mock_drop.assert_called_once()
    mock_insert.assert_called_once_with(status)
