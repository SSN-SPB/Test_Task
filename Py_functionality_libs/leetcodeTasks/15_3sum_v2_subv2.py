# https://leetcode.com/problems/3sum/description/
# version 2 2026-Feb-5 Pass
nums = [-1, 0, 1, 2, -1, -4]


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = sorted(nums)
        output = set()
        for k in range(len(s)):
            target = -s[k]
            i, j = k + 1, len(s) - 1
            while i < j:
                sum_two = s[i] + s[j]
                if sum_two < target:
                    i += 1
                elif sum_two > target:
                    j -= 1
                else:
                    output.add((s[k], s[i], s[j]))
                    i += 1
                    j -= 1
        return output


def main():
    c = Solution()
    print(f" longest prefix: {c.threeSum(nums)}")


if __name__ == "__main__":
    main()
