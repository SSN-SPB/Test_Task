# https://leetcode.com/problems/3sum/description/
# version 2 2026-Feb-3- Time Limit Exceeded 311/316

nums = [-1, 0, 1, 2, -1, -4]


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        final_list = []
        for t in range(2, len(nums)):
            # interim_list = []
            # print(f"third: {t}")
            for s in range(0, t):
                # interim_list = []
                # print(f"second: {s}")
                for f in range(0, s):
                    interim_list = []
                    if len(set([f, s, t])) == 3:
                        # print(f"first: {f}")
                        # print(f"second: {s}")
                        # print(f"third: {t}")
                        # if f != s and f != t and f != s:
                        # print(f"first: {f}")
                        # print(f"second: {s}")
                        # print(f"third: {t}")
                        if nums[f] + nums[s] + nums[t] == 0:
                            # print(f"first: {f}")
                            # print(f"second: {s}")
                            # print(f"third: {t}")
                            # interim_list.append(nums[t])
                            # interim_list.append(nums[s])
                            # interim_list.append(nums[f])
                            # if sorted(interim_list) not in final_list:
                            if sorted([nums[f], nums[s], nums[t]]) not in final_list:
                                final_list.append(sorted([nums[f], nums[s], nums[t]]))
                                # final_list.append(sorted(interim_list))
        return final_list


def main():
    c = Solution()
    print(f" longest prefix: {c.threeSum(nums)}")


if __name__ == "__main__":
    main()
