#!/usr/bin/env python3
# https://realpython.com/python-reduce-function/
from functools import reduce


def subtract_values(x, y):
    return y - x


def main():
    print(range(5))
    print(list(range(5)))
    print(reduce(subtract_values, [1, 2, 3]))
    print(reduce(subtract_values, range(6)))
    print(reduce(lambda x, y: x + y, range(6)))


if __name__ == "__main__":
    main()
