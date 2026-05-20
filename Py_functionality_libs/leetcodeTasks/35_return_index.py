# 35 https://leetcode.com/problems/search-insert-position/
# version 2026-May-19 Passes
import pytest


@pytest.mark.parametrize(
    "tested_list, tested_value",
    [([[1, 3, 5, 6], 7], 4), ([[1, 3, 5, 6], 5], 2)],
)
def test_position(tested_list, tested_value):
    if tested_list[0].count(tested_list[1]):
        result = list(tested_list[0]).index(tested_list[1])
    else:
        for x in tested_list[0]:
            if x > tested_list[1]:
                result = tested_list[0].index(x)
        result = len(list(tested_list[0]))
    assert result == tested_value


test_list = [1, 3, 5, 6]
test_value = 2


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums.count(target):
            return nums.index(target)
        else:
            for x in nums:
                if x > target:
                    return nums.index(x)
            return len(nums)


def main():
    c = Solution()
    print(f" result : {c.searchInsert(test_list, test_value)}")
    assert c.searchInsert(test_list, test_value) == 1


if __name__ == "__main__":
    main()
