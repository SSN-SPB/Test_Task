# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# version 2026-Mar-02 in progress failed 146/182
# s = "aaa"; words =["a","a"]
# Output [0]
# Expected [0,1]
from itertools import permutations

words_to_concatenate = ["a"]
checked_string = "a"
# words_to_concatanate = ["foo", "bar"]
# checked_string = "barfoothefoobarman"


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result_list = []
        if len(words) != 1 and len(set(words)) == 1 and len(s) == 1:
            return result_list
        if len(set(words)) == 1 and len(words) != 1 and len(set(s)) == 1:
            return [0]

        concatenation_list = list(permutations(words))
        concatenation_strings = []
        for x in range(0, len(concatenation_list)):
            concatenation_strings.append("".join(concatenation_list[x]))
        for y in range(0, len(s)):
            if y + len(concatenation_strings[0]) <= len(s):
                if s[y : y + len(concatenation_strings[0])] in concatenation_strings:
                    result_list.append(y)
        return result_list


def main():
    c = Solution()
    print(f" result : {c.findSubstring(checked_string, words_to_concatenate)}")
    assert c.findSubstring(checked_string, words_to_concatenate) == [0]


if __name__ == "__main__":
    main()
