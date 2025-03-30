#!/usr/bin/env python3
# Copyright 2021 Sergei Smirnov
# https://compscicenter.ru/courses/python/2015-autumn/classes/1542/
# 17:00
# yield - stop point in function


def gnr():
    print('start')
    x = 14
    # y = 'z'
    yield x
    print('print1: x={}'.format(x))
    x += 1
    yield x
    print('print2: x={}'.format(x))
    x += 1
    yield x
    print('print3: x={}'.format(x))
    x += 1
    yield x
    print(x)
    x += 1
    yield x
    print(x)


def main():
    gener = gnr()  # print('start') is not displayed because of yield
    next(gener)    # 1st yield print1: x=14
    next(gener)    # 2nd yield print2: x=15
    next(gener)    # 3d yield (if exists or exeption - StopIteration)
    next(gener)    # 3d yield (if exists or exeption - StopIteration)


if __name__ == '__main__':
    main()
