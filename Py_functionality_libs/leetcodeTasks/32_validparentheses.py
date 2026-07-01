# https://leetcode.com/problems/longest-valid-parentheses/description/
# version 2026-Mar-06
from sklearn.utils.estimator_checks import check_estimator_sparse_tag


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        valid_sting = "()"
        result = 0
        for x in range(0, len(s)-1):
            interim_result = 0
            checked_sting = s[x:x+2]
            if checked_sting == valid_sting:
                interim_result += 2
                x += 2
            else:
                interim_result = 0
            if interim_result > result:
                result = interim_result
        return result




tested_string32 = "(()"
tested_string32 = "(()()"


def main():
    c = Solution()
    print(f" result : {c.longestValidParentheses(tested_string32)}")
    assert c.longestValidParentheses(tested_string32) == 4


if __name__ == "__main__":
    main()
