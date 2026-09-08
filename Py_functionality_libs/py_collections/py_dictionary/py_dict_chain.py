# ChainMap is a class in the collections module that groups
# multiple dictionaries together to create a single, updateable view.
# It allows you to search through multiple dictionaries as if they were one,
# and it maintains the order of the dictionaries.
from collections import ChainMap

dict_test1 = {"a": 10, "b": 8}
dict_test2 = {"d": 6, "c": 4, "a": 7}
dict_test3 = {"e": 6, "t": 4, "y": 7}


def main():
    test_dict = ChainMap(dict_test1, dict_test2, dict_test3)
    print(test_dict["a"])  # 10
    print(test_dict["b"])
    print(test_dict["c"])
    print(test_dict["d"])
    print(test_dict["t"])
    print(test_dict)  # ChainMap({'a': 10, 'b': 8},
    # {'d': 6, 'c': 4, 'a': 7}, {'e': 6, 't': 4, 'y': 7})


if __name__ == "__main__":
    main()
