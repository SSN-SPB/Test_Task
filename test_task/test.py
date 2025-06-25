"""
This file contains 4 functions
that perform mains arithmetic actions
functions of addition, subtraction,
division and multiplication of two numbers
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def multiply(a, b):
    """Return the multiplication of two numbers."""
    return a * b


def subtract(a, b):
    """Return the subtraction of two numbers."""
    return a - b


def divide(a, b):
    """Return the division of two numbers."""
    return a / b


def main():
    """Print out example of using each function
    and making assertion the received value for each function
    """
    print("Add: 5 + 3 =", add(5, 3))
    print("Multiply: 4 * 6 =", multiply(4, 6))
    print("Substruct: 6 - 4 =", subtract(6, 4))
    print("Divide: 6 / 4 =", divide(6, 4))
    assert add(1, 4) == 5
    assert multiply(1, 4) == 4
    assert subtract(1, 4) == -3
    assert divide(6, 4) == 1.5


if __name__ == "__main__":
    main()
