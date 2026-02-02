# https://leetcode.com/problems/longest-palindromic-substring/
# version 2 2026-Jan-27 - Time Limit Exceeded

test_string = "cbbd"


def longestPalindrome(s):
    result = 0
    result_list = ""
    if s == s[::-1]:
        return s

    for x in range(0, len(s)):
        for y in list(range(0, len(s) + 1))[::-1]:
            test_list = list(s[x:y])
            if test_list == test_list[::-1]:
                if len(test_list) > result:
                    result = len(test_list)
                    result_list = test_list
    return "".join(result_list)


def main():
    assert longestPalindrome(s=test_string) == "bb"


if __name__ == "__main__":
    main()
