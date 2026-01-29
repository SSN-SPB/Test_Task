# https://leetcode.com/problems/palindrome-number/description/ 09


def isPalindrome(x: int) -> bool:
    interim_list = list(str(x))
    return interim_list[::-1] == interim_list


def main():
    assert not isPalindrome(26)
    assert isPalindrome(121)
    assert not isPalindrome(-121)


if __name__ == "__main__":
    main()
