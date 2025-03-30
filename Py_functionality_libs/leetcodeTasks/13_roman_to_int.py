# https://leetcode.com/problems/roman-to-integer/description/ 13


def romanToInt(s: str) -> int:
    list_of_string = list(s)
    print(len(list_of_string))
    result_sum = 0
    y = -1
    while y < len(list_of_string) - 1:
        y = y + 1
        if list_of_string[y] == "M":
            result_sum = result_sum + 1000
            continue
        if list_of_string[y] == "D":
            result_sum = result_sum + 500
            continue
        if list_of_string[y] == "C" and y + 1 < len(list_of_string):
            if list_of_string[y + 1] == "M":
                result_sum = result_sum + 900
                y = y + 1
                continue
        if list_of_string[y] == "C" and y + 1 < len(list_of_string):
            if list_of_string[y + 1] == "D":
                result_sum = result_sum + 400
                y = y + 1
                continue
        if list_of_string[y] == "C":
            result_sum = result_sum + 100
            continue
        if list_of_string[y] == "L":
            result_sum = result_sum + 50
            continue
        if list_of_string[y] == "X" and y + 1 < len(list_of_string):
            if list_of_string[y + 1] == "C":
                result_sum = result_sum + 90
                y = y + 1
                continue
        if list_of_string[y] == "X" and y + 1 < len(list_of_string):
            if list_of_string[y + 1] == "L":
                result_sum = result_sum + 40
                y = y + 1
                continue
        if list_of_string[y] == "X":
            result_sum = result_sum + 10
            continue
        if list_of_string[y] == "V":
            result_sum = result_sum + 5
            continue
        if list_of_string[y] == "I" and y + 1 < len(list_of_string):
            if list_of_string[y + 1] == "X":
                result_sum = result_sum + 9
                break
            if list_of_string[y + 1] == "V":
                result_sum = result_sum + 4
                break
        if list_of_string[y] == "I":
            result_sum = result_sum + 1
            continue
    print("final sum: " + str(result_sum))

    return result_sum


def main():
    assert romanToInt("XX") == 20
    assert romanToInt("V") == 5
    assert romanToInt("IV") == 4
    assert romanToInt("IX") == 9
    assert romanToInt("VII") == 7
    assert romanToInt("MCMXCIV") == 1994
    assert romanToInt("DCXXI") == 621
    assert romanToInt("MMMXLV") == 3045


if __name__ == "__main__":
    main()
