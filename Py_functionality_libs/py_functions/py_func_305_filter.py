roll = [24, 1, 4, 2, 9, 17, 27, 37, 47, 57]


def main():
    result_list = list(filter(lambda x: x % 3 == 0, roll))
    print(result_list)
    assert result_list == [24, 9, 27, 57]


if __name__ == "__main__":
    main()
