# https://leetcode.com/problems/integer-to-roman/ 12

romanMap = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
}


class Solution:
    def intToRoman(self, num: int) -> str:
        result_string = []
        # result_string = ""
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while n <= num:
                result_string.append(romanMap[n])
                num -= n
            print(n)
        print(result_string)
        return "".join(result_string)


def main():
    c = Solution()
    assert c.intToRoman(91) == "XCI"
    assert c.intToRoman(4) == "IV"
    assert c.intToRoman(5) == "V"
    assert c.intToRoman(15) == "XV"
    assert c.intToRoman(40) == "XL"
    assert c.intToRoman(50) == "L"
    assert c.intToRoman(51) == "LI"
    assert c.intToRoman(52) == "LII"
    assert c.intToRoman(56) == "LVI"
    assert c.intToRoman(100) == "C"
    assert c.intToRoman(156) == "CLVI"
    assert c.intToRoman(200) == "CC"
    assert c.intToRoman(300) == "CCC"
    assert c.intToRoman(3000) == "MMM"
    assert c.intToRoman(3000) == "MMM"
    assert c.intToRoman(3300) == "MMMCCC"


if __name__ == "__main__":
    main()


# def intToRoman(self, num: int) -> str:
#   valueSymbols = [(1000, 'M'), (900, 'CM'),
#                   (500, 'D'), (400, 'CD'),
#                   (100, 'C'), (90, 'XC'),
#                   (50, 'L'), (40, 'XL'),
#                   (10, 'X'), (9, 'IX'),
#                   (5, 'V'), (4, 'IV'),
#                   (1, 'I')]
#   ans = []
#
#   for value, symbol in valueSymbols:
#     if num == 0:
#       break
#     count, num = divmod(num, value)
#     ans.append(symbol * count)
#
#   return ''.join(ans)
