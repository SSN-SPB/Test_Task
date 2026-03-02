"""Suit for demo of itertools"""

# itertools.compress() - creates an iterator that filters elements
# from data returning only those that have a corresponding element
# in the selectors that evaluates to True.
# Stops when either the data or selectors iterables has been exhausted.

from itertools import compress

test_list = ["A", "B", "C", "D", "E", "F", "J"]
compress_mask = [
    1,
    0,
    1,
    0,
    1,
    1,
    0,
    1,
    1,
    0,
    1,
    0,
    1,
    0,
]


def check_itertools_compress(tested_list, mask_list):
    """Function removes elements from list based on mask"""
    print(f"tested list: {tested_list}")

    return list(compress(tested_list, mask_list))


def main():
    result_list = check_itertools_compress(test_list, compress_mask)
    print(result_list)
    assert result_list == ["A", "C", "E", "F"]


if __name__ == "__main__":
    main()
