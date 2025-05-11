"""Suit for demo of itertools"""

import itertools
import random

# creating list of random length with randomly sorted values
created_list = list(range(3, random.randint(7, 33)))
test_list = list(set(created_list[0 :: random.randint(2, 7)]))


def check_itertools_accumulate(tested_list):
    """Function iterates list and accumulate the integer values"""
    print(tested_list)
    # Create list of accumulated values
    print(list(itertools.accumulate(tested_list)))
    print(tested_list)


def main():
    """Function to be run 1st"""
    print(check_itertools_accumulate.__doc__)
    check_itertools_accumulate(test_list)


if __name__ == "__main__":
    main()
