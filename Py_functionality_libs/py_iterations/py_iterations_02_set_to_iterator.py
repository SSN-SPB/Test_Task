#!/usr/bin/env python3


def main2():
    set2 = {1, "a", 2, 3, 6, 12}
    print(set2)
    try:
        print(next(set2))
    except TypeError as te:
        print("no iterator yet")
        print(te)
    iter1 = iter(set2)
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
    # print(dir(StopIteration))


if __name__ == "__main__":
    main2()
