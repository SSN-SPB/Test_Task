# 58 https://leetcode.com/problems/length-of-last-word/
# version 2026-May-20 Passes
import pytest

s1 = "Hello World"


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])


def main():
    c = Solution()
    print(f" result : {c.lengthOfLastWord(s1)}")
    assert c.lengthOfLastWord(s1) == 5


@pytest.mark.parametrize(
    "tested_string, tested_value",
    [("Hello World", 5), ("Hello World  ", 5), ("Hello Tim  ", 3)],
)
def test_check_last_word(tested_string, tested_value):
    c = Solution()
    assert c.lengthOfLastWord(tested_string) == tested_value


def test_check_last_word2():
    c = Solution()
    assert c.lengthOfLastWord(s1) == 5


def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5


if __name__ == "__main__":
    main()
