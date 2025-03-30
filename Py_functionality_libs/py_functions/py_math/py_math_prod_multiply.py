import math
import unittest

test_tuple = (1, 7, 2, 6, 3)


class MyTestCase(unittest.TestCase):
    def test_multiply(self):
        result = math.prod(test_tuple)
        self.assertEqual(result, 252)  # add assertion here


if __name__ == "__main__":
    unittest.main()
