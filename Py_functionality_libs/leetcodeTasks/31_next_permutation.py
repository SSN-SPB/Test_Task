# https://leetcode.com/problems/next-permutation/
# version 2026-Mar-05 passes locally but fails on leetcode
from itertools import permutations


# input_list = [1,1,5]
# input_list = [3,2,1]
input_list = [1, 2, 3]
# output_list = [1,5,1]
# output_list = [1,2,3]
output_list = [1, 3, 2]


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # print(list(permutations(nums)))
        # return list(list(permutations(nums))[-1])
        interim_list = sorted(
            permutations(nums)
        )  # all permutations in lexicographic order
        current = tuple(nums)

        current_index = interim_list.index(current)
        print(f"interim_list: {interim_list}")
        print(f"current: {current}")
        print(f"current_index: {current_index}")

        # return next permutation or wrap to first
        if current_index + 1 < len(interim_list):
            return list(interim_list[current_index + 1])
        else:
            return list(interim_list[0])


def main():
    c = Solution()
    print(f" result : {c.nextPermutation(input_list)}")
    # assert c.nextPermutation(input_list) == output_list


if __name__ == "__main__":
    main()
