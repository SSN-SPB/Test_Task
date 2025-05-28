#!/usr/bin/env python3

# https://www.tutorialsteacher.com/python/python-package

import os
import time
import datetime
import git

# import ssn is mandatory
import ssn

from ssn import print_line as pl


def main():
    print("Package_checking")
    ssn.print_line.print_message("Hello package")
    pl.print_message("Hello package2")


if __name__ == "__main__":
    main()
