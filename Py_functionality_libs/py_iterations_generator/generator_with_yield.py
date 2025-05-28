#!/usr/bin/env python3
# Copyright 2021 Sergei Smirnov
# https://compscicenter.ru/courses/python/2015-autumn/classes/1542/
# 25:10
# yield - stop point in function
# https://docs.python.org/3/library/itertools.html list of available iterators

x = [1, 7, 2, 3, 4, 1, 3, 3, 4, 7]


def gnr(iterator, seen=None):
    if seen is None:
        seen = set()
    z = 1
    for i in iterator:
        if i not in seen:
            print("z is: {}".format(z))
            seen.add(i)
            print(seen)
            z += 1
            yield i


def main():
    c = gnr(x)
    w = 0
    try:
        while w < len(x):
            next(c)
            w += 1
    except StopIteration as si:
        # print(dir(si))
        print(si.__doc__)
        # print(si.value)
        # print(si.__dict__)


if __name__ == "__main__":
    main()
