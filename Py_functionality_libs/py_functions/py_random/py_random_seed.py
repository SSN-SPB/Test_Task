"""random.seed() guaranties the same random value"""

import random


def random_sample_seed():
    random.seed("x", 4)
    return random.randint(1, 100)


def random_random():
    return random.randint(1, 100)


def main():
    print(random_random())
    print(random_random())
    print(random_random())
    print(random_random())
    print("Same values:")
    print(random_sample_seed())
    print(random_sample_seed())
    print(random_sample_seed())
    print(random_sample_seed())


if __name__ == "__main__":
    main()
