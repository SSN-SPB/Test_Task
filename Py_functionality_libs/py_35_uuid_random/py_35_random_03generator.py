# This script demonstrates the use of the random module
# in Python 3.5 to generate a list of random integers.
# It uses a fixed seed for reproducibility.


import random


def main():
    rng = random.Random(42)
    values = [rng.randint(1, 100) for _ in range(5)]
    print(values)


if __name__ == "__main__":
    main()
