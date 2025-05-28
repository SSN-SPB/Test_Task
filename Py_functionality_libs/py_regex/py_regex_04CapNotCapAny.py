#!/usr/bin/env python3
import re

# Write a Python Program to find sequences of one upper case letter
# followed by lower case letters. If found, print ‘Yes’, otherwise ‘No’.

regex = "[A-Z][a-z]"


# function for checking the string
def check(string):
    # pass the regular expression
    # and the string in the search() method
    if re.search(regex, string):
        print("{} - Yes".format(string))
    else:
        print("{} - No".format(string))


if __name__ == "__main__":
    sample1 = "abba"
    sample2 = "a"
    sample3 = "abcd"
    sample4 = "A3abcd"
    sample5 = "AAabcd"

    check(sample1)
    check(sample2)
    check(sample3)
    check(sample4)
    check(sample5)
