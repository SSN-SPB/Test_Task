#!/usr/bin/env python3

import os


# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/ ~36
# string find('ra', 0, 3) return index of first finding or -1

def main():

    strng = 'foo.bar.two.three.two.two__com'
    print('Checking find'.center(80, '/'))
    print(strng.find('two')) # 8 # first finiding
    print(strng.find('twoz')) # -1
    print(strng.find('two',0,3)) # -1 - not found ~ [:3].find('two')
    print(strng.find('two',10,203)) # 18
    # similar to index
    print(strng.index('two'))# 8 # first finiding
    # index not found returns exception
    # print(strng.index('twoz')) # ValueError: substring not found
    # finding from the end of line
    print(strng.find('two')) # 8 # first finiding
    print(strng.rfind('two'))# 22 # first from right part finiding
    
if __name__ == '__main__': result = main()

