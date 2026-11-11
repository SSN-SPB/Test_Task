# This script demonstrates the use of the random int module


import random


def main():
    values = [random.randint(1, 100) for _ in range(5)]
    print(values)


if __name__ == "__main__":
    main()
