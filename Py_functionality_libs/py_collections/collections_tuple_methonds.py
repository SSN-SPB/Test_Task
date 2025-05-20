#!/usr/bin/env python3


def compare_tuples(tuple_a, tuple_b):
    print(tuple_a.__dir__)
    print(tuple_b.__dir__)
    print("hash of tuple1 is {}".format(tuple_a.__hash__))
    print("hash of tuple2 is {}".format(tuple_a.__hash__))
    print("methods of tuple hash are {}".format(dir(tuple_b.__hash__)))
    print("doc of tuple hash are {}".format(tuple_b.__hash__.__doc__))
    print("name of tuple hash are {}".format(tuple_b.__hash__.__name__))
    print("tuples are equals {}".format(tuple_a == tuple_b))
    print("tuples are the same object {}".format(tuple_a is tuple_b))


def main2():
    print("list of tuple's methonds")
    for x in dir(tuple):
        print("attributes of tuple {}".format(x))
    tuple1 = (1, "aa", True)
    tuple2 = tuple1
    tuple3 = (1, "aa", True)
    compare_tuples(tuple1, tuple2)
    compare_tuples(tuple1, tuple3)
    print("-------- compare tuples with list ---------")
    tuple12 = (1, "a", True, ["c", "d"])
    tuple22 = tuple12
    tuple32 = (1, "a", True, ["c", "d"])
    compare_tuples(tuple12, tuple22)
    compare_tuples(tuple12, tuple32)


if __name__ == "__main__":
    main2()
