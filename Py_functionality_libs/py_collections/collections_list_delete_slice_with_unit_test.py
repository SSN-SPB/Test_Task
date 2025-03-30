# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# list 31:22
# delete
# slice [:2] first 2;
# slice [::-1] list in the reverse order;
# slice [::2] each 2nd;
# slice [:] - all
# slice [a[start:stop:step]
# slice [:] - all
#  +---+---+---+---+---+---+
#   | P | y | t | h | o | n |
#   +---+---+---+---+---+---+
#   0   1   2   3   4   5   6
#  -6  -5  -4  -3  -2  -1
import copy
import unittest
list2 = [30, 21, -2, 31, "4", 5, 6, 19]

#
# class MainTest(unittest.TestCase):
#     def test_list_slice(self):
#         updated_list = remove_every_third_from_list(list2)
#         self.assertEqual (updated_list, [30, -2, 31, 5, 6])


def remove_every_third_from_list(initial_list):
    new_list = copy.deepcopy(initial_list)
    del new_list[1::3]
    return new_list


def main():
    updated_list = remove_every_third_from_list(list2)
    print(list2)             # [30, 21, -2, 31, '4', 5, 6, 19]
    print(updated_list)      # [30, -2, 31, 5, 6]


if __name__ == "__main__":
    main()
    # unittest.main(verbosity=2)
