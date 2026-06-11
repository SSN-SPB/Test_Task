from unittest.mock import patch, Mock

from api_client import get_user


@patch("api_client.requests.get")
def test_get_user_success(mock_get):
    # Mock response data
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
    }

    # Inject mock response
    mock_get.return_value = mock_response

    # Call function
    result = get_user(1)

    # Assertions
    assert result["id"] == 1
    assert result["name"] == "John Doe"

    # Verify request was called correctly
    mock_get.assert_called_once_with(
        "https://api.example.com/users/1"
    )