# https://leetcode.com/problems/reverse-integer/description/ 10

import datetime
from datetime import datetime as dt


def isPalindrome(x: int) -> bool:
    interim_list = list(str(x))
    return interim_list[::-1] == interim_list


def main():
    assert isPalindrome(26) == False
    assert isPalindrome(121) == True
    assert isPalindrome(-121) == False


if __name__ == "__main__":
    main()
