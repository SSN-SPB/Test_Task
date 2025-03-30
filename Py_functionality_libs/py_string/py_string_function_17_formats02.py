#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ 46
# formats


def main():
    header_name = 'Hello world'
    header_name2 = 'Hello world2'
    print('{!s}'.format(header_name2))
    print('{!r}'.format(header_name2))
    print('{!r} - {!s}'.format(header_name2, header_name))
    print('{1!r} - {0!s}'.format(header_name2, header_name))


if __name__ == '__main__':
    main()
