#!/usr/bin/env python3

import os


# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/
# string split
# string partition (always returns 3 arguments tuple)
# string partition 1st arg - string before 1st 'split-argument
# string partition 2nd arg - 'split-argument
# string partition 3d arg - string after 1st 'split-argument


def main():
    print("Checking spliting treating".center(80, "/"))
    strng = "foo.bar.two.three.com"
    print(strng.split("."))  # ['foo', 'bar', 'two', 'three', 'com']
    print(
        "Getting file extension from"
        " foo.bar.two.three.com - rsplit - rigth split".center(80, "/")
    )
    print(strng.rsplit(".", 1))  # ['foo.bar.two.three', 'com']
    l = strng.rsplit(".", 1)
    print(l[1])  # com
    print(strng.split(".", 2))  # ['foo', 'bar', 'two.three.com']
    print("Spliting space by default".center(80, "/"))
    print("\t foo foo2 bar \r ".center(80, "/"))
    print("\t foo foo2 bar \r ".split())  # ['foo', 'foo2', 'bar']
    print("---".center(80, "/"))
    print("Partion".center(80, "/"))
    print("foo foo2 bar ".partition("."))  # ('foo foo2 bar ', '', '')
    print("Partion righ".center(80, "/"))
    print("foo foo2 bar ".rpartition("."))  # ('', '', 'foo foo2 bar ')
    print("Partion righ with existing spliter".center(80, "/"))
    print("foo ; foo2 ; bar ;".rpartition(";"))  # ('foo ; foo2 ; bar ', ';', '')
    print("Partion left with existing spliter".center(80, "/"))
    print("foo ; foo2 ; bar ;".partition(";"))  # ('foo ', ';', ' foo2 ; bar ;')


if __name__ == "__main__":
    result = main()
