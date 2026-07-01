# https://leetcode.com/problems/reverse-integer/
# version 2026-Apr-21 passes
int_x = 1230


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        list_int = list(str(int(abs(x))))[::-1]
        print(list_int)
        result_str = ""
        for y in list_int:
            result_str = result_str + str(y)
        if int(result_str) > 2**31 - 1 or -int(result_str) < -(2**31):
            return 0
        if x < 0:
            return -int(result_str)
        return int(result_str)


def main():
    c = Solution()
    print(f" result : {c.reverse(x=int_x)}")
    # assert c.convert(s=tested_string, numRows=num_rows) == expected_output


if __name__ == "__main__":
    main()
