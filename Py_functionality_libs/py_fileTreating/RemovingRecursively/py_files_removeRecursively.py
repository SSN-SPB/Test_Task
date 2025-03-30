#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


from pathlib import Path
import os
# remove files recursively



def main():
    # for path in Path('src').rglob('*.c'):
    # for path in Path('testing').rglob('*.java'):
    for path in Path('testing').rglob('*.*'):
        os.remove(path)
        print('The file {} is removed'.format(path))


if __name__ == '__main__': main()
