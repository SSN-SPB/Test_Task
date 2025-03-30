# https://leetcode.com/problems/integer-to-roman/ 12

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
    # 'C' : '100,
    # 'CD' : '400,
    # 'D' : '500',
    # 'CM' : '900',
    # 'M' : '1000'
}


def intToRoman(num: int) -> str:
    result_string = ""
    divided_to = 10
    num_rest = float("+inf")
    while divided_to < 10000 and num > 0:
        num_rest = int(num % divided_to)
        divided_to = divided_to * 10
        if num_rest > 0:
            result_string = romanMap[str(num_rest)] + result_string
        num = num - num_rest
        # final_str = ""
        # checked_int_list = list(str(num))[::-1]
        #     print(num)
        print("num {}, num_rest {}, str {}".format(num, num_rest, result_string))
    print("Final num {}, num_rest {}, str {}".format(num, num_rest, result_string))
    return result_string


def main():
    # assert intToRoman(91) == 'XCI'
    # assert intToRoman(4) == 'IV'
    # assert intToRoman(5) == 'V'
    # assert intToRoman(15) == 'XV'
    # assert intToRoman(40) == 'XL'
    # assert intToRoman(50) == 'L'
    # assert intToRoman(51) == 'LI'
    assert intToRoman(52) == "LII"
    assert intToRoman(56) == "LVI"
    assert intToRoman(100) == "C"
    assert intToRoman(156) == "CLVI"
    assert intToRoman(200) == "CC"
    assert intToRoman(300) == "CCC"


if __name__ == "__main__":
    main()
