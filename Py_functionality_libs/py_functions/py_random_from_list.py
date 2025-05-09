import random

list_to_test = [
    "x1",
    "x11",
    "x12",
    "x13",
    "x14",
    "x15",
    "x16",
    "x17",
]


def return_random_from_list(tested_list, number):
    return random.sample(tested_list, number)


def main():
    retrieved_list = return_random_from_list(list_to_test, 3)
    print(retrieved_list)
    assert len(retrieved_list) == 3


if __name__ == "__main__":
    main()
