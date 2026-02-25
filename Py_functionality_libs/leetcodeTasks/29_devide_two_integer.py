# https://leetcode.com/problems/divide-two-integers/
# version 2026-Feb-25 passed
import math


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor != 0:
            sign = (
                -1
                if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0)
                else 1
            )
            if dividend / divisor < 0:
                return min(
                    max(int(math.ceil(abs(dividend) / abs(divisor))) * sign, -(2**31)),
                    2**31 - 1,
                )
            else:
                return min(
                    max(int(math.floor(abs(dividend) / abs(divisor))) * sign, -(2**31)),
                    2**31 - 1,
                )


def main():
    c = Solution()
    print(f" result of division is : {c.divide(7, -3)}")


if __name__ == "__main__":
    main()
