#!/usr/bin/env python3
# Copyright 2021 Sergei Smirnov
# https://compscicenter.ru/courses/python/2015-autumn/classes/1542/
# 17:00
# itereable has no __next__
# Iterable is an object, which one can iterate over.

def main():
    # list of cities
    cities = ["Berlin", "Vienna", "Zurich"]

    # initialize the object
    iterator_obj = iter(cities)
    for x in iterator_obj:
        print(f'from iterable {x}')
    for x in iterator_obj:
        print(f'from iterable {x}')

    try:
        print(next(iterator_obj))
    except StopIteration as si:
        print('No more iterator')
    #
    for x in iterator_obj:
        print(x)
    for x in cities:
        print(f'from city {x}')



if __name__ == '__main__':
    main()
