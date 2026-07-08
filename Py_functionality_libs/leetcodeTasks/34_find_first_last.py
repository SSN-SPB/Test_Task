# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# 34. Find First and Last Position of Element in Sorted Array
nums = [5, 7, 7, 8, 8, 10]
target = 8


class Solution(object):
    def searchRange(self, nums: list, target: int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result_list = []
        if target in nums:
            result_list.append(nums.index(target))
        else:
            return [-1, -1]
        result_list.append(len(nums) - 1 - nums[::-1].index(target))

        return result_list


def main():
    c = Solution()
    print(f" result : {c.searchRange(nums, target)}")


if __name__ == "__main__":
    main()
