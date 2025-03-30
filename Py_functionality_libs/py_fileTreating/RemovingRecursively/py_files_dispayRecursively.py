#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


from pathlib import Path
# display files recursively



def main():
    # for path in Path('src').rglob('*.c'):
    for path in Path('testing').rglob('*.java'):
        print(path.name)    


if __name__ == '__main__': main()
