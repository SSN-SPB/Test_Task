list_for_key = ["apple", "orange", "grape"]


def print_dictionary_element(dictionary_to_print):
    print(dictionary_to_print)
    for k, v in dictionary_to_print.items():
        print(f"k - v is: {k} - {v}")


def main():
    test_dict = dict.fromkeys(list_for_key)
    print_dictionary_element(test_dict)
    test_dict["orange"] = "nice"
    print_dictionary_element(test_dict)

    test_dict2 = dict.fromkeys(list_for_key, "new")
    print_dictionary_element(test_dict2)
    test_dict2["apple"] = "nice"
    print_dictionary_element(test_dict2)

    test_dict3 = dict.fromkeys(list_for_key, [])
    print_dictionary_element(test_dict3)
    test_dict3["apple"] = "nice"
    print_dictionary_element(test_dict3)


if __name__ == "__main__":
    main()
