dict_test1 = {"a": 10, "b": 8}
dict_test2 = {"d": 6, "c": 4, "a": 7}


def merge_dict(dict1, dict2):
    res = dict1 | dict2
    return res


def main():
    dict_test3 = merge_dict(dict_test1, dict_test2)
    print(dict_test2)
    print(dict_test3)
    assert dict_test3 == {"d": 6, "c": 4, "a": 7, "b": 8}
    assert {"d": 6, "c": 4, "a": 7, "b": 8} == {"a": 7, "c": 4, "d": 6, "b": 8}


if __name__ == "__main__":
    main()
