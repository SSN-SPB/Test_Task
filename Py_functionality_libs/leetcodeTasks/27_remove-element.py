# https://leetcode.com/problems/remove-element/
# version 2026-Feb-10
tested_nums = [3, 2, 2, 3]


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # result_list = []
        # for x in nums:
        #     if x != val:
        #         result_list.append(x)
        # return result_list
        k = 0

        for x in nums:
            if x != val:
                nums[k] = x
                k += 1

        return k


def main():
    c = Solution()
    print(f" number of checked elements is : {c.removeElement(tested_nums, 3)}")


if __name__ == "__main__":
    main()
