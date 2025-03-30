# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/17
import itertools

digits_numbers = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
    "0": "_",
}


class Solution:
    def letterCombinations(self, digits) -> list:
        if digits == "":
            return []
        interm_list = list(digits)
        received_digits = []
        final_list = []
        for x in interm_list:
            received_digits.append(list(digits_numbers.get(x)))
        print("Received digits: {}".format(received_digits))
        combinations = list(itertools.product(*received_digits))
        for x in combinations:
            interim_string = ""
            print(x)
            for y in list(x):
                interim_string = interim_string + y
            final_list.append(interim_string)

        print(final_list)
        return final_list


def main():
    c = Solution()
    assert c.letterCombinations("23") == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]
    assert c.letterCombinations("2") == ["a", "b", "c"]
    assert c.letterCombinations("234") == [
        "adg",
        "adh",
        "adi",
        "aeg",
        "aeh",
        "aei",
        "afg",
        "afh",
        "afi",
        "bdg",
        "bdh",
        "bdi",
        "beg",
        "beh",
        "bei",
        "bfg",
        "bfh",
        "bfi",
        "cdg",
        "cdh",
        "cdi",
        "ceg",
        "ceh",
        "cei",
        "cfg",
        "cfh",
        "cfi",
    ]


if __name__ == "__main__":
    main()
