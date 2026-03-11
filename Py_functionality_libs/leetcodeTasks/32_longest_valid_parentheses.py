# https://leetcode.com/problems/longest-valid-parentheses/description/ #32
# version 2026-Mar-10


tested_string = ["(()", 2]
# tested_string = ["(()())", 4]
# tested_string = [")()())", 4]
# tested_string = [")(",0]

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        direct = "("
        reversed = ")"
        result = 0
        tested_length = len(s)
        if tested_length == 1:
            return result
        for x in range(0, tested_length):
            print(s[x])
            if s[x] == direct and s[x + 1] == reversed:
                result += 1
                x += 2
                continue
            if s[x] == reversed:
                tested_length -= 2
                break
            if s[x] == direct and s[len(s) - 1 - x] == reversed:
                result += 1
                tested_length -= 2
                break
        return result * 2


def main():
    c = Solution()
    print(f" result : {c.longestValidParentheses(tested_string[0])}")
    assert c.longestValidParentheses(tested_string) == tested_string[1]


if __name__ == "__main__":
    main()
