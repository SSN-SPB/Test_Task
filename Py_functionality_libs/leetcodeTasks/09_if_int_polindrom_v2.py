# https://leetcode.com/problems/palindrome-number/description/ 09
# version 2 2026-Jan-29- Passes

test_string = "cbbd"


class Solution(object):
    def isPalindrome(self, x):
        if x >= 0:
            list_string_x = list(str(x))
            print(list_string_x)
            if list_string_x == list_string_x[::-1]:
                return True
            return False
        else:
            return False


def main():
    c = Solution()
    print(c.isPalindrome(x=523))
    print(c.isPalindrome(x=55))
    print(c.isPalindrome(x=515))
    print(c.isPalindrome(x=-515))
    print(c.isPalindrome(x=10))


if __name__ == "__main__":
    main()
