#!/usr/bin/env python3


import sys


def main(*args):
    print(
        "This script counts sum of first two int"
        " arguments of script {}".format(sys.argv[0])
    )
    argum = []
    a, b = 0, 0
    for x in args[0]:
        argum.append(x)
    if len(argum) > 1:
        try:
            if argum[1]:
                a = float(argum[1])
                print("argument 1 is {}".format(a))
            if argum[2]:
                b = float(argum[2])
                print("argument 2 is {}".format(b))
        except Exception as e:
            print("one of values is not a digit. Reason: {}".format(e))
        print("The final sum is {:.2f}".format(a + b))
    else:
        print("The required argument is not found")


try:
    if __name__ == "__main__":
        main(sys.argv)
except IndexError:
    main()
