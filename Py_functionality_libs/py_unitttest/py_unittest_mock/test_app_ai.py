import unittest
from unittest.mock import patch
from app_ai import get_user_data

class TestGetUserData(unittest.TestCase):

    @patch('app_ai.requests.get')  # Mocking the requests.get method in the app module
    def test_get_user_data_success(self, mock_get):
        # Mock response object
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"id": 1, "name": "John Doe"}

        result = get_user_data(1)
        self.assertEqual(result, {"id": 1, "name": "John Doe"})
        mock_get.assert_called_once_with("https://api.example.com/users/1")

    @patch('app_ai.requests.get')
    def test_get_user_data_not_found(self, mock_get):
        # Simulate a 404 response
        mock_get.return_value.status_code = 404

        result = get_user_data(2)
        self.assertEqual(result, {"error": "User not found"})
        mock_get.assert_called_once_with("https://api.example.com/users/2")


if __name__ == '__main__':
    unittest.main()