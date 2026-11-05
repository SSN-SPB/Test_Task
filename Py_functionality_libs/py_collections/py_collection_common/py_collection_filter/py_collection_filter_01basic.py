test_list = [1, 7, 2, 9, 11, 8, 4, 7, 6, 15]


def divide_to_n(n):
    return lambda x: x % n == 0


def main():
    for x in range(1, 10):
        print(x)
        selected_list = list(filter(divide_to_n(x), test_list))
        print(selected_list)


if __name__ == "__main__":
    main()
