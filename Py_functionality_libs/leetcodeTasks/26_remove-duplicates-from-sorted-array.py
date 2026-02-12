# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# version 2 2026-Feb-11 Works well but Output Limit Exceeded - 78 / 362 testcases passed
# tested_nums = [0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4]
# tested_nums = [0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4]
tested_nums = [1, 1, 2]
# tested_nums = [1, 1]
# tested_nums = [-50,-50,-49,-49,-48,-46,-46,-46,-46,-45,-45,-44,-44,-43,-42,-42,-42,-42,-41,-41,-39,-39,-39,-39,-38,-38,-38,-37,-36,-36,-36,-36,-35,-35,-34,-34,-34,-32,-32,-32,-30,-30,-29,-29,-28,-28,-28,-27,-27,-26,-25,-25,-24,-24,-23,-23,-22,-22,-21,-21,-20,-20,-19,-19,-18,-18,-18,-18,-17,-15,-15,-14,-14,-13,-13,-12,-12,-12,-12,-11,-11,-10,-10,-10,-8,-8,-8,-7,-7,-7,-7,-6,-6,-3,-3,-2,-2,-2,-1,1,1,2,3,4,4,5,5,5,6,6,6,7,9,9,9,10,10,10,10,11,12,13,14,14,14,15,16,16,17,17,18,19,19,19,20,20,20,21,21,21,21,21,21,24,24,24,25,25,26,26,26,27,27,27,28,28,29,29,29,30,30,31,33,33,33,33,34,34,34,34,35,38,38,38,40,41,42,43,44,44,45,45,46,46,46,46,46,46,47,47,47,48,49,49,49,49]


class Solution(object):
    @staticmethod
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for x in nums:
            while nums.count(x) > 1:
                nums.remove(x)
        return len(nums)
        # The second passed solution
        # expected_size = len(list(set(nums)))
        # for x in nums:
        #     while nums.count(x) > 1:
        #         nums.remove(x)
        # return expected_size

        ## The third solution: It works well but
        ## Output Limit Exceeded - 78 / 362 testcases passed
        # expected_size = len(list(set(nums)))
        # if expected_size == 1:
        #     return expected_size
        # k = len(nums) - 1
        # while k > 0:
        #     while nums[k] == nums[k - 1]:
        #         print(nums[k])
        #         nums.pop(k)
        #         k = len(nums) - 1
        #     k -= 1
        #     print(nums)
        # return expected_size


def main():
    c = Solution()
    print(tested_nums)
    print(f" number of unique elements: {c.removeDuplicates(tested_nums)}")
    print(tested_nums)
    # assert c.removeDuplicates(tested_nums) == 5


if __name__ == "__main__":
    main()
