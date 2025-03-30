#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ 46
# formats


def main():
    header_name = 'formats_var'
    print(' formats '.center(79, '/'))
    print(' {} '.center(79 - len(header_name), '/').format(header_name))
    print('int: {0:d} hex: {0:x}'.format(42))  # int: 42 hex: 2a
    print('{:-^16}'.format('Hi'))              # -------Hi-------
    print('{0} {who} - {who} {0}'.format('Hi', who='Pek'))  # Hi Pek - Pek Hi
    point = {'x': -7, 'y': 5}
    print('x = {0[x]}, y = {0[y]}'.format(point))  # x = -7, y = 5


if __name__ == '__main__':
    main()
