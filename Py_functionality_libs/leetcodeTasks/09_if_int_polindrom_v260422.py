# https://leetcode.com/problems/palindrome-number/description/ 09
# version 2026-Apr-22- Passes

test_string = "cbbd"


class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        string_from_number = list(str(abs(x)))
        return string_from_number == string_from_number[::-1]


def main():
    c = Solution()
    assert not c.isPalindrome(x=-515)
    assert not c.isPalindrome(x=-10)
    assert not c.isPalindrome(x=523)
    assert c.isPalindrome(x=515)
    assert c.isPalindrome(x=55)


if __name__ == "__main__":
    main()
