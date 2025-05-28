#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ 35:10
# find index

# https://www.geeksforgeeks.org/python-string-find/
# The find() method returns the lowest index of the
# substring if it is found in given string.
# If its is not found then it returns -1.
# Syntax :
#
# str.find(sub,start,end)
#
# Parameters :

# sub : It’s the substring which needs to be searched in the given string.
# start : Starting position where sub is needs to be checked within the string.
# end : Ending position where suffix is needs to be checked within the string.


def main():
    print(" string in not_in funtion ".center(79, "/"))
    s = "blablablazoobla"
    checked_string = "bla"
    print(s.find(checked_string))  # 0
    print(s.find(checked_string, 2))  # 3
    print(s.find(checked_string, 3, 17))  # 3
    print("not foudn string returns -1 ".ljust(79, "/"))
    print(s.find("xxxx", 3, 17))  # -1
    print("index for not foudn string returns exception ".ljust(79, "/"))
    try:
        print(s.index("xxxx", 8, 17))
    except Exception as e:
        print(e)  # substring not found
    try:
        print(s.index("bla", 8, 17))  # 12
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
