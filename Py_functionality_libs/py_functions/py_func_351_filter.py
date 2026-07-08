roll = [24, 1, 4, 2, 9, 17, 27, 37, 47, 57]
roll2 = [24, 1, 4, 2, 9, 17, 27, 37, 47, 57]


def main():
    result_list = list(filter(lambda x: x % 3 == 0, roll))
    result_list2 = list(filter(lambda x: x + x > 10, roll2))
    print(f" result_list: {result_list}")
    print(result_list2)
    assert result_list == [24, 9, 27, 57]


if __name__ == "__main__":
    main()
