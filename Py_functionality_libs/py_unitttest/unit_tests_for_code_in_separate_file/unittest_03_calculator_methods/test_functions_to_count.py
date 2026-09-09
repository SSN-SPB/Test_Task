import unittest

from count_functions import count_sum


class TestSumCount(unittest.TestCase):

    def test_sum_count(self):
        result = count_sum(3, 7)
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main()
