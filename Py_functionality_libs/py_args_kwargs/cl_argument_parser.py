#!/usr/bin/env python3

import argparse
import sys

# running cl: python cl_argument_parser.py -b 12 -a 27
# to display help -run cl: python cl_argument_parser.py -h
# https://docs.python.org/3.3/library/argparse.html
# https://www.youtube.com/watch?v=cdblJqEUDNo


def main():
    print(
        "This script counts sum of first two"
        " arguments of script {}".format(sys.argv[0])
    )
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--first_value", type=int, help="First argument")
    parser.add_argument("-b", type=int, help="Second argument")
    args = vars(parser.parse_args())
    print(args)

    if (args.get("first_value") or args.get("a")) and args.get("b"):
        function_calculate(args.get("first_value"), args.get("b"))
    else:
        print("The required arguments are not defined")
        print("The default values are used")
        function_calculate()


def function_calculate(a=0, b=0):
    x = a + b
    # print ('a value is {}, type is {}'.format(a,type(a)))
    print("The final sum is {:.2f}".format(x))


if __name__ == "__main__":
    main()
