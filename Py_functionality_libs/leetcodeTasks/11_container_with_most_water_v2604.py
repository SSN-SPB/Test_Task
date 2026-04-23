# https://leetcode.com/problems/container-with-most-water/
# version 2026-Apr-21 passes
tested_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result_volume = 0
        for x in height:
            for y in range(height.index(x) + 1, len(height)):
                # print(f" index:{y} element: {height[y]} previous element {x}")
                result_volume = max(
                    min(x, height[y]) * (y - height.index(x)), result_volume
                )
                # interim_result = min(x, height[y]) * (y - height.index(x) )
                # if interim_result > result_volume:
                #     result_volume = interim_result
        return result_volume


def main():
    c = Solution()
    print(f" result : {c.maxArea(height=tested_list)}")
    assert c.maxArea(height=tested_list) == 49


if __name__ == "__main__":
    main()
