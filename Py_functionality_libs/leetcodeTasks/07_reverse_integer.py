# https://leetcode.com/problems/reverse-integer/description/ 07

import datetime
from datetime import datetime as dt


def reverse(x: int) -> int:
    interim_list = list(str(abs(x)))
    reversed_list = interim_list[::-1]
    str_new = ""
    for y in reversed_list:
        str_new = str_new + y
    if int(str_new) > 2**31 - 1 or -int(str_new) < -(2**31):
        return 0
    if int(x) > 0:
        return int(str_new)
    return -int(str_new)


def main():
    assert reverse(26) == 62
    assert reverse(-26) == -62
    assert reverse(1534236469) == 0


if __name__ == "__main__":
    main()
