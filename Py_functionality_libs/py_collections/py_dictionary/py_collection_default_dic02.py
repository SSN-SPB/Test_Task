"""
automatically provides a default value for
missing keys, instead of raising a KeyError.
"""

from collections import defaultdict

grouped_dictionary = defaultdict(int)

words = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple",
    "apple",
    "peach",
    "apple",
]


def count_default_dic(tested_list, test_default_dic):
    for item in tested_list:
        test_default_dic[item] += 1
    return test_default_dic


def main():
    print(f"default_dict {grouped_dictionary}")
    print(dict(count_default_dic(words, grouped_dictionary)))
    print(f"updated {grouped_dictionary}")


if __name__ == "__main__":
    main()
