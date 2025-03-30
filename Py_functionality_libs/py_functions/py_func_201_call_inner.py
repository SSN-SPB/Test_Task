#!/usr/bin/env python3
# https://www.geeksforgeeks.org/python-map-function/

numbers1 = [1, 2, 3, 1, 11]
numbers2 = (4, 5, 6, 99)


def outer_function(x):
    def inner_function(y):
        return x * y

    return inner_function


def main():
    result = outer_function(4)(5)
    print(result)


if __name__ == "__main__":
    main()
