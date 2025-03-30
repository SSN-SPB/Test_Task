dict_test1 = {"a": 10, "b": 8}
dict_test2 = {"d": 6, "c": 4, "a": 7}


def merge_dict(dict1, dict2):
    res = {**dict2, **dict1}
    return res


def main():
    dict_test3 = merge_dict(dict_test1, dict_test2)
    print(dict_test2)
    print(dict_test3)


if __name__ == "__main__":
    main()
