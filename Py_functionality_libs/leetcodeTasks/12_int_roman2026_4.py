# https://leetcode.com/problems/integer-to-roman/ 12
# 2026-04-24 passed need to optimize

romanMap = {
    "1": "I",
    "4": "IV",
    "5": "V",
    "9": "IX",
    "10": "X",
    "40": "XL",
    "50": "L",
    "90": "XC",
    "100": "C",
    "400": "CD",
    "500": "D",
    "900": "CM",
    "1000": "M",
}


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        final_list = sorted(list(romanMap.keys()), key=int)[::-1]
        result_string = ""
        while num > 0:
            if num > int(final_list[0]) - 1:
                result_string += romanMap[final_list[0]]
                num -= int(final_list[0])
                if num < int(final_list[0]):
                    del final_list[0]
                if num == 0:
                    return result_string
                # print(final_list)
            while num < int(final_list[0]):
                del final_list[0]
        return result_string


def main():
    c = Solution()
    print(f" result : {c.intToRoman(3749)}")


if __name__ == "__main__":
    main()
