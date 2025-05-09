"""Suit for demo of itertools"""

from itertools import compress

# creating list of random length with randomly sorted values
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
    print(tested_list)

    return list(compress(tested_list, mask_list))


def main():
    result_list = check_itertools_compress(test_list, compress_mask)
    print(result_list)
    assert result_list == ["A", "C", "E", "F"]


if __name__ == "__main__":
    main()
