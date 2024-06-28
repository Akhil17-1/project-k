import pytest
from agent import update_status
from unittest.mock import patch, MagicMock
import agent

@patch.dict(agent.__dict__, {'db': MagicMock()})
def test_update_status():
    """Test updating status."""
    # Mocking the collection
    mock_collection = MagicMock()

    # Setting up the return values for the db mock
    agent.db.status = mock_collection

    status = {"Application": "Collected"}

    # Call the function
    update_status(status)

    # Assertions
    try:
        mock_collection.drop.assert_called_once()
        print("mock_collection.drop.assert_called_once() passed")
    except AssertionError as e:
        print(f"mock_collection.drop.assert_called_once() failed: {e}")

    try:
        mock_collection.insert_one.assert_called_once_with(status)
        print("mock_collection.insert_one.assert_called_once_with(status) passed")
    except AssertionError as e:
        print(f"mock_collection.insert_one.assert_called_once_with(status) failed: {e}")

    assert mock_collection.drop.call_count == 1, f"Expected drop to be called once, but it was called {mock_collection.drop.call_count} times."
    assert mock_collection.insert_one.call_count == 1, f"Expected insert_one to be called once, but it was called {mock_collection.insert_one.call_count} times."

if __name__ == "__main__":
    pytest.main()
