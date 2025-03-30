dictionary_test = {"a": 100, "b": 200, "c": 300}


def return_sum(dict_to_test):
    res = 0
    for i in dict_to_test.values():
        res = res + i
    return res


def main():
    print("Sum :", return_sum(dictionary_test))


if __name__ == "__main__":
    main()
