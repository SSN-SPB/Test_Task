#!/usr/bin/env python3
# https://www.geeksforgeeks.org/python-map-function/
# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.

numbers1 = [1, 2, 3, 1, 11, 15]
numbers2 = (4, 5, 6, 99)


def increase_seven(x):
    return x + 7


def main():
    print(list(map(lambda x: x + 100, range(10))))
    print(list(map(increase_seven, range(10))))
    print(list(map(lambda x, y: x + y, numbers1, numbers2))) # [5, 7, 9, 100]
    # value 11 and 15 from numbers1 are ignored
    # because numbers2 has only 4 elements


if __name__ == "__main__":
    main()
