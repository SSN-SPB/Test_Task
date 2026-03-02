"""
Use the math.isclose() function to check if two floating-point
numbers are close to each other.
"""

import math

a = 0.1 + 0.2
b = 0.3


def main():
    print(f"Is a close to b? {a} and {b} are close: {math.isclose(a, b)}")
    print(f"Is a equal to b? {a} and {b} are equal: {a == b}")


if __name__ == "__main__":
    main()
