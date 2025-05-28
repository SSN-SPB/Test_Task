#!/use/bin/env python3

import sys
import useful


# https://compscicenter.ru/courses/python/2015-autumn/classes/1556/ 0 - 14


def main():
    # print(dir(sys))
    useful.print_boo()
    print(sys.platform)
    print(sys.__name__)
    print(useful)
    for x in dir(useful):
        print(x)
        m = str(x)
        print(useful)


if __name__ == "__main__":
    main()
