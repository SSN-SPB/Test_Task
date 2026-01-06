# What is output
import os
import time
import datetime


def print_all_variable():
    a = '12_34'
    b = float(a)
    print(b)
    assert b == 1234.0


def main():
    print_all_variable()


if __name__ == "__main__":
    main()

