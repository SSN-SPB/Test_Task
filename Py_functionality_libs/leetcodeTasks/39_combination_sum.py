# https://leetcode.com/problems/combination-sum/description/
# 39. Combination Sum
candidates = [2,3,6,7]
target = 6


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort(reverse=True)
        print(candidates)
        list_of_lists = []
        for x in range(0, len(candidates)):
            current_value = candidates[x]
            if min(candidates) > target:
                return list_of_lists
            print(int(target / current_value))
            multiplier = int(target / current_value)
            if target % current_value == 0:
                list_of_lists.append([current_value] * multiplier)
            # while multiplier >= 1:
            #     target = target - current_value
            #     multiplier -=1
            #     if (current_value * multiplier + candidates[x])


        return list_of_lists



def main():
    c = Solution()
    print(f" result : {c.combinationSum(candidates, target)}")


if __name__ == "__main__":
    main()
