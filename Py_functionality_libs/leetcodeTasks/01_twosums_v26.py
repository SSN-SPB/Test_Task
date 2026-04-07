# https://leetcode.com/problems/two-sum/

import datetime
from datetime import datetime as dt

nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    result_list = []
    for x in range(0, len(nums) - 1):
        for y in range(x + 1, len(nums)):
            if nums[x] + nums[y] == target:
                result_list.append(x)
                result_list.append(y)
                break
    return result_list

def main():
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([3,2,4], 6))
    #
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3,2,4], 6) == [1, 2]



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
