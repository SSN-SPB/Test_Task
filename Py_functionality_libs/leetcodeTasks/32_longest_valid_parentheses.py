# https://leetcode.com/problems/longest-valid-parentheses/description/ #32
# version 2026-Mar-10


tested_string = "(()())"

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        direct = "("
        reversed = ")"
        result = 0
        for x in range(0, int(len(s)/2)):
            if tested_string[x] == direct and tested_string[len(s) - 1 - x] == reversed:
                result += 1
        return result


def main():
    c = Solution()
    print(f" result : {c.longestValidParentheses(tested_string)}")
    assert c.longestValidParentheses(tested_string) == 3


if __name__ == "__main__":
    main()
