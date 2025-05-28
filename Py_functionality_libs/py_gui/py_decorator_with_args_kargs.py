#!/usr/bin/env python3
# Copyright 2021 Sergei Smirnov


def basic_decorator(func):
    print("function {} starts".format(func.__name__))

    def function_treating(*args, **kwargs):
        print("Starting function {}".format(func.__name__))
        result = func(*args, **kwargs)
        print("Result is {}".format(result))
        print("Completing function {}".format(func.__name__))
        return result

    print("function {} completed".format(func.__name__))
    return function_treating


def calculate_sum(a, b, c=7, d=8):
    sum_result = a + b
    # print('internal_function')
    sum_two = c + d
    return sum_result, sum_two


def main():
    # calculate_sum(3, 5)
    decorator_result = basic_decorator(calculate_sum)
    decorator_result(3, 5)
    decorator_result(1, 2, c=3, d=5)


if __name__ == "__main__":
    main()
