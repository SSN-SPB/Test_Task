"""Suit for demo of itertools"""

import itertools

# itertools.product() - creates an iterator that returns the
# cartesian product of input iterables.
# Equivalent to nested for-loops in a generator expression.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

from itertools import product

tested_string_one = "ABC"
tested_string_two = "DEF"
expected_list = [
    ("A", "D"),
    ("A", "E"),
    ("A", "F"),
    ("B", "D"),
    ("B", "E"),
    ("B", "F"),
    ("C", "D"),
    ("C", "E"),
    ("C", "F"),
]


def create_itertools_product(string_one, string_two):
    """Function creates cartesian product of 2 strings"""
    print(f"tested strings: {string_one} and {string_two}")
    for x in itertools.product(string_one, string_two):
        print(x)

    return list(product(string_one, string_two))


def main():
    result = create_itertools_product(tested_string_one, tested_string_two)
    print(result)
    assert result == expected_list


if __name__ == "__main__":
    main()
