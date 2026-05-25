# input data
set1 = {1, 2, 3, 5, 4}
collection2 = {1, 3, 4}
collection3 = [1, 4, 9, 15, 11, 7, 1]


def intersection(test_instance, *args):
    return set(test_instance).intersection(*args)


def main():
    result = intersection(set1, collection2, collection3)
    print(result)
    assert result == {1, 4}


if __name__ == "__main__":
    main()
