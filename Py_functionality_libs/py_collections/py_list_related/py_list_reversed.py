list_to_test = [1, 2, 3, 4, 5, 6, 7]


def reversed_list(test_list):
    return reversed(test_list)


def main():
    result_sum = list(reversed_list(list_to_test))
    print(result_sum)  # [7, 6, 5, 4, 3, 2, 1]


if __name__ == "__main__":
    main()
