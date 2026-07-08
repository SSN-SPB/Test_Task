# cProfile is a built-in Python module that provides
# a way to profile the performance of Python code.
# It allows you to measure the time
# taken by different parts of your code and identify bottlenecks.
import cProfile


def my_function():
    a = 1
    b = 1
    assert a == b
    pass


cProfile.run("my_function()")


def main():
    cProfile.run("my_function()")


if __name__ == "__main__":
    main()
