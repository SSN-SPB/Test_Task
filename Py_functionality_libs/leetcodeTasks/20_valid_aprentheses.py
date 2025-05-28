# https://leetcode.com/problems/valid-parentheses/description/


class Solution:
    def isValid(self, s):
        final_list = list(s)
        return_result = True
        if len(final_list) % 2 != 0:
            return False
        list_keys = ["(", "[", "{"]
        list_values = [")", "]", "}"]
        # test_dict = {"(": ")", "[": "]", "{": "}"}
        for x in range(0, int(len(final_list) / 2)):
            # print(len(final_list) / 2)
            print(x)
            print("print x element {}".format(final_list[x]))
            print("print -x element {}".format(final_list[-x - 1]))
        print("final list 1/2: {}".format(final_list[: -x - 1]))
        for y in final_list[: -x - 1]:
            print(y)

        print(final_list)

        return True


def main():
    c = Solution()
    print(c.isValid("([])"))


if __name__ == "__main__":
    main()
