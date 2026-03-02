#!/usr/bin/env python3
import re

testedRegexNumber = "\\d+"
stringTest = "This335IsGeeksforGeeks !, 123"


def check_string(str):
    numbers = re.findall(testedRegexNumber, str)
    numbers = map(int, numbers)
    return max(numbers)


def main():
    print(check_string(stringTest))


if __name__ == "__main__":
    main()
