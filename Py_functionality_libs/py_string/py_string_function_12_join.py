#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ 30:10
# join requires argument

def main():
    print('string join funtion'.center(79, '/'))
    s = ', '
    print(s.join(['x1', 'x2', 'x3']))     # x1, x2, x3


if __name__ == '__main__':
    main()
