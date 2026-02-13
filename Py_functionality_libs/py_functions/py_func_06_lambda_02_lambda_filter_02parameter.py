tested_list = list(range(0, 11))


def lambda_one_more_other(y):
    return lambda x: x > y


def main():
    more_then_3 = lambda_one_more_other(3)
    # using lamda in filter
    print(list(filter(more_then_3, tested_list)))
    assert list(filter(more_then_3, tested_list)) == [4, 5, 6, 7, 8, 9, 10]


if __name__ == "__main__":
    main()
