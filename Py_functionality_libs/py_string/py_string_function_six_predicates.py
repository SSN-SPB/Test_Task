#!/usr/bin/env python3

import os
import re

# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ ~40
# 

def main():

    strng = 'foo.bar.two.three.two.two__com'
    print('Checking predicats'.center(80, '/'))
    print('result 1 is {}'.format(strng.isdigit())) # result 1 is False
    print(strng.isalpha()) # False
    print('result 3 is {}'.format(strng.isalnum())) # result 3 is False
    print(strng.islower()) # True
    print('result 5 is {}'.format(strng.isupper())) # result 5 is False
    print(strng.istitle()) # False
if __name__ == '__main__': result = main() 

