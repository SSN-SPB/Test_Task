# https://leetcode.com/problems/two-sum/

import datetime
from datetime import datetime as dt

nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    result_sum = []
    for x in range(0, len(nums)):
        for y in range(1, len(nums)):
            if nums[x] + nums[y] == target and x != y:
                result_sum.append(x)
                result_sum.append(y)
                break
    print(list(set(result_sum)))
    return list(set(result_sum))


def main():
    # result = twoSum(nums, target)
    # assert result == [0, 1]
    assert twoSum([2, 7, 11, 15], 26) == [2, 3]
    assert twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]


if __name__ == "__main__":
    main()


# version 2 2026-Jan-27
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for x in nums:
#             for y in range(nums.index(x)+1,len(nums)):
#                 if x + nums[y] == target:
#                     return [nums.index(x), y]
