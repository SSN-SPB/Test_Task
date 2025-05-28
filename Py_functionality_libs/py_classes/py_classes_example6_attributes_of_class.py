#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1477/
# class 14:00
# parent classes
# import traceback
# import sys
# if class has __slots__ - exemplar has no __dict_

list1 = [1, 2, 9]
tuple2 = (3, 5, 11)


def sample_map(colection1, collection2):
    print(list(map(lambda x, y: x - y, colection1, collection2)))


def main2():
    sample_map(list1, tuple2)


if __name__ == "__main__":
    main2()
