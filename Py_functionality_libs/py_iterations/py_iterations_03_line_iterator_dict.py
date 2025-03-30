#!/usr/bin/env python3


def compare_tuples(range_limit):
    dict1 = {number: number**2 for number in range(range_limit)}
    print(dict1)
    return dict1


def main2():
    list2 = compare_tuples(5)
    assert list2 == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


if __name__ == "__main__":
    main2()
