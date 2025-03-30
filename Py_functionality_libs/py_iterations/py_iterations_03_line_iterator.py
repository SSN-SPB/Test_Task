#!/usr/bin/env python3


def compare_tuples(range_limit):
    list1 = [number**2 for number in range(range_limit)]
    print(list1)
    return list1


def main2():
    list2 = compare_tuples(5)
    assert list2 == [0, 1, 4, 9, 16]


if __name__ == "__main__":
    main2()
