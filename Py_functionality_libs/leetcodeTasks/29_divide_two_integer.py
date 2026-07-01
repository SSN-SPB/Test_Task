# https://leetcode.com/problems/divide-two-integers/
# version 2026-Feb-25 passed


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        condition_one = dividend >= 0 and divisor < 0
        condition_two = dividend < 0 and divisor >= 0
        sign = -1 if condition_one or condition_two else 1
        return min(max(int(abs(dividend) / abs(divisor)) * sign, -(2**31)), 2**31 - 1)


def main():
    c = Solution()
    print(f" result of division is : {c.divide(7, -3)}")
    assert c.divide(7, -3) == -2


if __name__ == "__main__":
    main()
