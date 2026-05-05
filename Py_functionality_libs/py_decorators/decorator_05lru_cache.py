# The @lru_cache decorator in Python is a built-in decorator from the functools module that provides a simple way to cache the results of expensive function calls. It stands for "Least Recently Used Cache" and is used to optimize performance by storing the results of function calls and returning the cached result when the same inputs occur again. This can significantly speed up functions that are called frequently with the same arguments, such as recursive functions like Fibonacci.

import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_no_cache(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    n = 455

    start = time.time()
    fibonacci_no_cache(n)
    logger.info(f"With No cache: {(time.time() - start) * 1000} ms")

    start = time.time()
    fibonacci(n)
    logger.info(f"With cache: {(time.time() - start) * 1000} ms")


if __name__ == "__main__":
    main()
