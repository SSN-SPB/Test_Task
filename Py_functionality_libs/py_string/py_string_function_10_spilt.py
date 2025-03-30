#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ 26:10


def main():
    print('split funtion'.center(79, '/'))
    s = 'foo.x1.x2.x3.mp4'
    print('init: {}'.format(s))
    print(s.split())        # ['foo.x1.x2.x3.mp4'] 
    print(s.split('.'))     # ['foo', 'x1', 'x2', 'x3', 'mp4']
    print(s.split('.', 1))  # ['foo', 'x1.x2.x3.mp4']
    print(s.split('.', -1)) # ['foo', 'x1', 'x2', 'x3', 'mp4']
    print('split starting from right'.center(79, '/'))
    print(s.rsplit('.', 1)) # ['foo.x1.x2.x3', 'mp4']

if __name__ == '__main__':
    main()
