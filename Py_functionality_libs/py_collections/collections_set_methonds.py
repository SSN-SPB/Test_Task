#!/usr/bin/env python3


def compare_sets(set_a, set_b):
    print(set_a.__dir__)
    print(set_b.__dir__)
    print("hash of set is {}".format(set_a.__hash__))
    print("hash of set is {}".format(set_b.__hash__))
    print("sets are equals {}".format(set_a == set_b))
    print("sets are the same object {}".format(set_a is set_b))


def main2():
    for x in dir(set):
        print("attributes of set {}".format(x))
    set1 = {1, "a", True, (1, 2), 7.8}
    print(x)
    print(set1)
    set2 = set1.copy()
    compare_sets(set1, set2)
    set3 = set1
    compare_sets(set1, set3)
    try:
        print(set1[0])
    except TypeError as te:
        print(te)
        print("index is not supported for set")
    print(set1)
    print(set2)
    print(set3)


if __name__ == "__main__":
    main2()
