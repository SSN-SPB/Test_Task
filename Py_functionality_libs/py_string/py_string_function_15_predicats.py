#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ 40:10
# predicats


def main():
    print(' predicats '.center(79, '/'))
    s = 'blablablazoobla'
    checked_string = 'bla'
    print(s.isdigit())            # False
    print(s.islower())            # True
    print(s.upper())              # BLABLABLAZOOBLA
    print(s.isupper())            # False


if __name__ == '__main__':
    main()
