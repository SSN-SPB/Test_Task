#!/usr/bin/env python3
# https://www.geeksforgeeks.org/python-map-function/

numbers1 = [1, 2, 3, 1, 11]
numbers2 = (4, 5, 6, 99)


def increase_seven(x):
    return x + 7


def main():
    print(list(map(lambda x: x + 100, range(10))))
    print(list(map(increase_seven, range(10))))
    print(list(map(lambda x, y: x + y, numbers1, numbers2)))


if __name__ == "__main__":
    main()
