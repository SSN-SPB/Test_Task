# https://leetcode.com/problems/longest-common-prefix/description/
# version 2 2026-Feb-2- Passes

test_string_list = ["flower", "flow", "flight"]
test_string_list = ["cir", "car"]


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        final_str = ""
        minimal_length = float("inf")
        # print(len(strs))
        for x in strs:
            if len(x) < minimal_length:
                minimal_length = len(x)
        for y in range(minimal_length):
            test_list = []
            for i in range(len(strs)):
                test_list.append(strs[i][y])
            # print(test_list)
            # print(test_list[0])
            # print(len(set(test_list)))
            if len(set(test_list)) == 1:
                final_str += test_list[0]
            else:
                return final_str
        return final_str


def main():
    c = Solution()
    print(f" longest prefix: {c.longestCommonPrefix(test_string_list)}")


if __name__ == "__main__":
    main()
