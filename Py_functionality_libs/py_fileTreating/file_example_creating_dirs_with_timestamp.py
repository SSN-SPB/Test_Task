#!/usr/bin/env python3

import os
import time
import datetime


def main():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    print(st)
    makedir(st,postfix='jdn')
    makedir(st,postfix='jdi_light')
    
def makedir(ts,prefix='clone',postfix='temp'):
    name_of_dir=prefix + str(ts) + postfix
    os.mkdir(name_of_dir)


if __name__ == '__main__': main()
