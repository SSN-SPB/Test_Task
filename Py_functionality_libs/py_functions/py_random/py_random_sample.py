import random

init_list = ["x1", "x2", "x3", "x4", "x5", "x6", "x7"]


def random_sample(tested_list, x):
    return random.sample(tested_list, x)


def main():
    print(random_sample(init_list, 3))
    assert len(random_sample(init_list, 3)) == 3


if __name__ == "__main__":
    main()
