# https://pynative.com/python-tuple-exercise-with-solutions/
tuple1 = (("a", 23), ("b", 37), ("c", 11), ("d", 29))
expected_tuple = (("c", 11), ("a", 23), ("d", 29), ("b", 37))


def sort_by_second(test_tuple):
    print(list(sorted(list(tuple1), key=lambda x: x[1])))
    return tuple(sorted(list(tuple1), key=lambda x: x[1]))


def main():
    tuple2 = sort_by_second(tuple1)
    print(tuple2)
    assert tuple2 == expected_tuple


if __name__ == "__main__":
    main()
