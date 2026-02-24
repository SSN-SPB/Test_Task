# https://leetcode.com/problems/divide-two-integers/
# version 2026-Feb-24 it works locally but not on leetcode -  2nd case failed
import math


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # < -2 ** 31
        if divisor != 0:
            if dividend/divisor < 0:
                return math.ceil(dividend/divisor)
            else:
                return math.floor(dividend / divisor)

def main():
    c = Solution()
    print(f" result of division is : {c.divide(7, -3)}")


if __name__ == "__main__":
    main()
