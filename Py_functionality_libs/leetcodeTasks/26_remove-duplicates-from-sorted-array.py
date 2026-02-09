# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# version 2 2026-Feb-9 Unclear Requirements
tested_nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
tested_nums = [1, 1, 2]


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(sorted(list(set(nums))))
        return sorted(list(set(nums)))[:size]


def main():
    c = Solution()
    print(f" number of unique elements: {c.removeDuplicates(tested_nums)}")
    # assert c.removeDuplicates(tested_nums) == 5


if __name__ == "__main__":
    main()
