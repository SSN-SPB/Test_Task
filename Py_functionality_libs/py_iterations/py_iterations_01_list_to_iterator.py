#!/usr/bin/env python3


def main2():
    list2 = [1, 2, 3, 6, 12]
    print(list2)
    try:
        print(next(list2))
    except TypeError as te:
        print("no iterator yet")
        print(te)
    iter1 = iter(list2)
    print(iter1)
    print(dir(iter1))
    print(iter1.__sizeof__())
    try:
        print("first element is {}".format(next(iter1)))
        print("the next element is {}".format(next(iter1)))
        print("the next element is {}".format(next(iter1)))
        print("the next element is {}".format(next(iter1)))
        print("the next element is {}".format(next(iter1)))
        print("the next element is {}".format(next(iter1)))
        print("the next element is {}".format(next(iter1)))
        print("the next element is {}".format(next(iter1)))
        print("the next element is {}".format(next(iter1)))
        print("the next element is {}".format(next(iter1)))
        print("the next element is {}".format(next(iter1)))
    except StopIteration as se:
        print("there is no the next element")
        print(se.__doc__)
    print(dir(StopIteration))


if __name__ == "__main__":
    main2()
