from operator import *

test_list = [10, 121, -7, 11]


def maximal_in_list(list: test_list) -> int:
    return sorted(test_list)[len(test_list) - 1]


def main():
    print(maximal_in_list(test_list))


if __name__ == "__main__":
    main()
