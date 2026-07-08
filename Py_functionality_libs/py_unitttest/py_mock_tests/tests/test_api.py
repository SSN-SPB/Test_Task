from unittest.mock import patch
import unittest
from app.app import get_user


class TestAPI(unittest.TestCase):
    @patch("app.app.requests.get")
    def test_get_user(self, mock_get):
        mock_get.return_value.json.return_value = {"id": 1, "name": "Alice"}

        result = get_user(1)

        self.assertEqual(result["name"], "Alice")


if __name__ == "__main__":
    unittest.main()
