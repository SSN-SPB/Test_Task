# https://leetcode.com/problems/3sum-closest/description/ 16


class Solution:
    def threeSumClosest(self, nums, target) -> int:
        closest = float("+inf")
        interim_value = float("+inf")
        result = float("-inf")
        for i in range(0, len(nums) - 2):
            for x in range(1, len(nums) - 1):
                for y in range(2, len(nums)):
                    if i != x and x != y and y != i:
                        calculated = nums[i] + nums[x] + nums[y]
                        interim_value = abs(target - calculated)
                        if closest > interim_value:
                            # closest = calculated
                            closest = interim_value
                            result = calculated
                    print(closest)
        print(closest)
        return result


def main():
    c = Solution()
    # assert c.threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert c.threeSumClosest([1, 1, 1, 1], 3) == 3
    # assert c.threeSumClosest([1, 1, 1, 0], -100) == 2


if __name__ == "__main__":
    main()
