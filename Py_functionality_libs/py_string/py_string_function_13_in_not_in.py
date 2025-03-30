#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ 34:10
# join requires argument

def main():
    print(' string in not_in funtion '.center(79, '/'))
    s = 'zz_yy'
    checked_string = 'foo'
    print(checked_string in s)         # False
    print(checked_string not in s)     # True
    print(s.startswith('z'))           # True
    print(s.endswith('z'))             # False
    print(' startswith endswith true if any of tuple - true '.center(79, '/'))
    print(s.endswith(('z', 'y')))      # True


if __name__ == '__main__':
    main()
