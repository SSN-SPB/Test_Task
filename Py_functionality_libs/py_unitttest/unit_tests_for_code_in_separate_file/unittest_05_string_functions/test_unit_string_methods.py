import unittest
from string_methods import define_string_length

class TestStringMethod(unittest.TestCase):

    def test_check_length(self):
        result_length = define_string_length("Hello")
        self.assertEqual(result_length, 5)

if __name__ == "__main__":
    unittest.main()