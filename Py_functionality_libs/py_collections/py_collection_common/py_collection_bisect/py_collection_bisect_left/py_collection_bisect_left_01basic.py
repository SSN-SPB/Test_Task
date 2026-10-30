# bisect_left() is a function from the built-in bisect module.
# It is used to find the position where an element should be inserted
# into an already sorted list, while keeping the list sorted.
#
# The important point is that bisect_left() does not insert anything
# into the list. It only returns an insertion index.

from bisect import bisect_left

tested_list = [10, 20, 50, 70, 80, 100]


def main():
    required_position = bisect_left(tested_list, 81)
    print(required_position)
    assert required_position == 5


if __name__ == "__main__":
    main()
