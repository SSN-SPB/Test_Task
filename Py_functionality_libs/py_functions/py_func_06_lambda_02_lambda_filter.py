tested_list = list(range(0, 9))


def more_then_three(x):
    return x > 3


def main():
    print(tested_list)
    # using lamda in map
    print(list(filter(lambda x: x > 3, tested_list)))
    assert list(filter(more_then_three, tested_list)) == [4, 5, 6, 7, 8]


if __name__ == "__main__":
    main()
