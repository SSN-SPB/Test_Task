from operator import *

test_list = [10, 1, -7, 11]


def minimal_in_list(list: test_list) -> int:
    return min(test_list)


def main():
    print(minimal_in_list(test_list))


if __name__ == "__main__":
    main()
