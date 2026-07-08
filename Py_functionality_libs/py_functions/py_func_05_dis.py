# https://compscicenter.ru/courses/python/2015-autumn/classes/1542/
import dis
# dis is a built-in Python module that allows you to analyze
# the bytecode of Python functions. It provides a
# way to inspect the low-level instructions that
# the Python interpreter executes when running your code.
# This can be useful for understanding how your code is executed,
# optimizing performance, and debugging.

tested_list = ["a", "b", "c"]


def sample_function(test_list):
    for x in test_list:
        print(x)
        print(x + x)


def main():
    sample_function(tested_list)
    dis.dis(sample_function)


if __name__ == "__main__":
    main()
