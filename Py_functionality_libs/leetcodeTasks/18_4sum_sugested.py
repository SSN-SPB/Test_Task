# https://leetcode.com/problems/4sum/description/


class Solution:
    def fourSum(self, nums, target) -> list:
        nums.sort()
        res = []

        for i in range(len(nums) - 3):
            # skip duplicate starting values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                # skip duplicate starting values
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, len(nums) - 1

                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if four_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif four_sum < target:
                        left += 1
                    else:
                        right -= 1
        return res


def main():
    c = Solution()
    print(c.fourSum([1, 0, -1, 0, -2, 2], 0))
    # assert c.fourSum([1, 0, -1, 0, -2, 2], 0) == [
    #     [-2, -1, 1, 2],
    #     [-2, 0, 0, 2],
    #     [-1, 0, 0, 1],
    # ]


if __name__ == "__main__":
    main()
