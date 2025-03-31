"""Suite demonstrates default dictionary for booleann"""

from collections import defaultdict


class DefaultDictionaryBoolean:
    """__ph__"""

    def __init__(self):
        self.boolean_dict = defaultdict(bool)

    def create_boolean_default_dictionary(self):
        return self.boolean_dict

    def display_dict_items(self):
        for k, v in self.boolean_dict.items():
            print(k, v)


def main():
    boolean_dictionary = DefaultDictionaryBoolean()
    boolean_one = boolean_dictionary.create_boolean_default_dictionary()
    print(boolean_one[1])
    boolean_one[1] = True
    print(boolean_one[1])
    # for k, v in boolean_one.items():
    #     print(k)
    #     print(v)
    boolean_dictionary.display_dict_items()

    boolean_two = boolean_dictionary.create_boolean_default_dictionary()
    print(boolean_two[12])
    boolean_two[12] = True
    print(boolean_two[12])
    boolean_dictionary.display_dict_items()


if __name__ == "__main__":
    main()
