"""Suit for demo of itertools"""

import itertools
import random


def creating_random_length_list():
    """creating list of random length with randomly sorted values"""
    created_list = list(range(3, random.randint(7, 33)))
    return list(set(created_list[0:: random.randint(2, 7)]))


def check_itertools_accumulate(tested_list):
    """Function iterates list and create list
    of allowed combination of elements as tupes"""
    print(tested_list)
    # Create list of element combinations
    print(list(itertools.combinations_with_replacement(tested_list, 4)))


def main():
    """Function to be run 1st"""
    print(check_itertools_accumulate.__doc__)
    check_itertools_accumulate(creating_random_length_list())


if __name__ == "__main__":
    main()
