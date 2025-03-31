from collections import defaultdict


class DefaultDictionaryBoolean:
    def create_boolean_default_dictionary(self):
        return defaultdict(bool)

    @staticmethod
    def display_dict_items(boolean_dict):
        for k, v in boolean_dict.items():
            print(k, v)


def main():
    boolean_dictionary = DefaultDictionaryBoolean()
    boolean_one = boolean_dictionary.create_boolean_default_dictionary()
    print(boolean_one[1])  # Default value (False)
    boolean_one[1] = True
    print(boolean_one[1])  # Now True

    # Call display_dict_items to print items
    DefaultDictionaryBoolean.display_dict_items(boolean_one)


if __name__ == "__main__":
    main()
