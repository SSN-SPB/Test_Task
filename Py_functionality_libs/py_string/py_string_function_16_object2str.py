#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ 44
# str repl ascii


def main():
    print(str('This is string'))  # This is string
    print(repr('This is string')) # 'This is string'
    s = ascii('This is string')
    print(s)                      # 'This is string' - expected like \\u0003f
    print('{!s}'.format('This is string'))            # This is string
    print('{!r}'.format('This is string'))            # 'This is string'
    print('{!a}'.format('This is string'))            # 'This is string'


if __name__ == '__main__':
    main()
