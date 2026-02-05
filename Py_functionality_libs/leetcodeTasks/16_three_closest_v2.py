# https://leetcode.com/problems/3sum-closest/description/
# version 2 2026-Feb-5
tested_nums = [-1,2,1,-4]
# tested_nums = [10,20,30,40,50,60,70,80,90]


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s = sorted(nums)
        print(s)
        for k in range(len(s)):
            i, j = k + 1, len(s) - 1
            result = float('inf')
            while i < j:
                sum_three = s[k] + s[i] + s[j]
                if sum_three - target < result:
                    result = sum_three - target
                    final_sum = sum_three
                if sum_three - target < 0:
                    i += 1
                elif sum_three - target > 0:
                    j -= 1
                else:
                    return sum_three
        return final_sum


def main():
    c = Solution()
    print(f" closest sum: {c.threeSumClosest(tested_nums, 1)}")


if __name__ == "__main__":
    main()
