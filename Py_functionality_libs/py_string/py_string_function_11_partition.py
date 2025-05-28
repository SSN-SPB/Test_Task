#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ 29:10
# partition requires argument


def main():
    print("partition funtion".center(79, "/"))
    s = "foo.x1.x2.x3.mp4"
    print("init: {}".format(s))
    try:
        print(s.partition())  # ['foo.x1.x2.x3.mp4']
    except Exception as e:
        print(e)
        print("Parition requires argument - s.partition() is ignore")
    print("partition returns tuple of 3 elements")
    print(s.partition("."))  # ('foo', '.', 'x1.x2.x3.mp4')
    print("if splitter is not found it returns the 1st element is string")
    print(s.partition(","))  # ('foo.x1.x2.x3.mp4', '', '')
    print("rpartition do the same from right side")
    print(s.rpartition(","))  # ('', '', 'foo.x1.x2.x3.mp4')


if __name__ == "__main__":
    main()
