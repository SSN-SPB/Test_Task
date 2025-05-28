# https://leetcode.com/problems/4sum/description/


class Solution:
    def fourSum(self, nums, target) -> list:
        final_list = []
        nums.sort()
        print(nums)
        for x in range(len(nums) - 3):
            for y in range(x + 1, len(nums) - 2):
                for w in range(y + 1, len(nums) - 1):
                    for q in range(w + 1, len(nums)):
                        if nums[x] + nums[y] + nums[w] + nums[q] == target:
                            if len(set([x, y, w, q])) == 4:
                                interim_list = sorted(
                                    [nums[x], nums[y], nums[w], nums[q]]
                                )
                                if interim_list not in final_list:
                                    final_list.append(interim_list)
        return final_list


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
