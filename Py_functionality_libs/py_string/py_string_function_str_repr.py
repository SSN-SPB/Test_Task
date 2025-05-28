#!/usr/bin/env python3

import os
import re

## https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ ~43
## https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ ~46
## str - returns the readable value
## repr - returns the object's image that allows restore the object


def main():

    print(str("I am string"))  # I am string
    print(repr("I am string"))  # 'I am string'
    print(ascii("I am string"))  # 'I am string'
    r = ascii("I am string ascii")
    print(r)  # 'I am string ascii' ???? - expected likee "'\\u044f \\u0441... '"
    s = "I am new string"
    print(str(s))  # I am new string
    print(repr(s))  # 'I am new string'
    print("format: {!r}".format(s))  # format: 'I am new string'
    print("format: {!s}".format(s))  # format: I am new string
    print("format: {!a}".format(s))  # format: 'I am new string'
    ## https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ ~46
    ## ':' at the end of format
    print("Format specifing demo".center(80, "/"))
    print("format: {:~^50}".format(s))  # format: 'I am new string'
    # format: ~~~~~~~~~~~~~~~~~I am new string~~~~~~~~~~~~~~~~~~
    print("format: {:+08.2f}".format(43.43))  # format: +0043.43
    print("format: {:^+18.2f}".format(43.43))  # format:       +43.43
    print("format: {:/^+18.2f}".format(43.43))  # format: //////+43.43//////


if __name__ == "__main__":
    result = main()
