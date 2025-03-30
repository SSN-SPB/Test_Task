#!/usr/bin/env python3

import os
import re

# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ ~37
# two(three optional) arguments (source, replacing, number of find replacing)

def main():

    strng = 'foo.bar.two.three.two.two__com'
    print('Checking replacing'.center(80, '/'))
    print(strng.replace('two', 't*o')) # foo.bar.t*o.three.t*o.t*o__com
    print(strng.replace('two', 't*o', 2)) # foo.bar.t*o.three.t*o.two__com
    print(strng.replace('two', 't*o', 2))
    print('Checking replacing via regexp'.center(80, '/'))
    s = "123123"
    s = re.sub('23$', 'penguins', s) # 1231penguins
    print(s)
    s = "123123"
    s = re.sub('^12', 'penguins', s)# penguins3123
    print(s)
    print('Checking replacing via slicing'.center(80, '/'))
    s = "1231234"
    print(s[::-1].replace('2','p',1)[::-1]) # 1231p34
    s = "1231234"
    print(s[::-1].replace('32','pu',1)[::-1]) # 1231up4
    s = "1231234"
    print(s.replace('23','pu',1)[::-1]) # 4321up1    
    
if __name__ == '__main__': result = main() 

