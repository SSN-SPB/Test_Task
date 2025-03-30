#!/usr/bin/env python3
import re

pattern = "[123]"
pattern2 = "123"


def check_string(pat, str):
    if re.search(pat, str):
        print('found')
    else:
        print('not found')


def main():
    check_string(pattern, '222')
    check_string(pattern, '2225')
    check_string(pattern2, '2225')
    check_string(pattern, 'a')


if __name__ == '__main__':
    main()
