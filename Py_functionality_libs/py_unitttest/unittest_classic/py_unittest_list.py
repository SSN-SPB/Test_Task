import unittest as unit
from unique_list import unique_order, expected_result

numbers = [1, 2, 2, 3, 4, 3, 5, 1]


class UnitList(unit.TestCase):
    def test_positive_list(self):
        self.assertEqual(unique_order(numbers), [1, 2, 3, 4, 5])

    def test_positive_list_two(self):
        self.assertEqual(unique_order(numbers), expected_result)


if __name__ == "__main__":
    unit.main()
