#!/usr/bin/env python3

import os
import string

# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ ~48
# format
# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ ~55
# string
# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ ~57
# bytes
# bytes works with bytes only:  'boo' in b'boobar' - TypeError


def main():
    # ':' at the end of format
    print('Format by key demo'.center(80, '/'))
    print('{0} , {why}, {0}'.format('because', why = 'where'))
    # response:  because , where, because
    points = 2, 7
    print('x = {0[0]} , y = {0[1]}'.format(points)) # x = 2 , y = 7
    points = {'x': 5, 'y': 24}
    print('x = {0[x]} , y = {0[y]}'.format(points)) # x = 5 , y = 24
    print('Module string demo'.center(80, '/'))
    print(string)
    print('Module string letters'.center(80, '/'))
    print(string.ascii_letters)    
    print('Module string letters[10]'.center(80, '/'))
    print(string.ascii_letters[10])
    print('Module string punctuation'.center(80, '/'))
    print(string.punctuation)
    print('Module string whitespace'.center(80, '/'))
    print(string.whitespace)
    print('Module bytes'.center(80, '/'))
    print('Я строка'.encode("utf-8"))
    # response:
    # b'\xd0\xaf \xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xba\xd0\xb0'
    print('Я строка'.encode("cp1251"))
    # response:
    # b'\xdf \xf1\xf2\xf0\xee\xea\xe0'
    print(b'boo' in b'boobar') # True
    
    
if __name__ == '__main__': result = main() 

