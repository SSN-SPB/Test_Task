#!/usr/bin/env python3

import os


# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ ~34.30
# string startwith endwith in


def main():

    strng = "foo.bar.two.three.com"
    print("Checking starstwith".center(80, "/"))
    print(strng.startswith(("two", "foo")))  # True
    print("Checking endswith".center(80, "/"))
    print(strng.endswith(("two", "foo")))  # False
    print(strng.endswith(("two", "com")))  # True
    print("Checking string in".center(80, "/"))
    print("two" in strng)  # True
    print("nine" in strng)  # False


if __name__ == "__main__":
    result = main()
