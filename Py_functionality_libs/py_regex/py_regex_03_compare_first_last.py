#!/usr/bin/env python3
import re

regex = '[A-Z][a-z]'


# function for checking the string
def check(string):
    # pass the regular expression
    # and the string in the search() method
    if (re.search(regex, string)):
        print("Valid")
    else:
        print("Invalid")


if __name__ == '__main__':
    sample1 = "abba"
    sample2 = "a"
    sample3 = "abcd"

    check(sample1)
    check(sample2)
    check(sample3)
