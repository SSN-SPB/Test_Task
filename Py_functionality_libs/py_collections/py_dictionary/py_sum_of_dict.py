dictionary_test = {"a": 100, "b": 200, "c": 300}


def count_number_elements_in_dict(func):
    def wrapper(test_dic):
        v = len(test_dic.values())
        print(f"The total number of elements is: {v}")
        return func(test_dic)

    return wrapper


@count_number_elements_in_dict
def return_sum(dict_to_test):
    res = 0
    for i in dict_to_test.values():
        res = res + i
    return res


def main():
    print("Sum :", return_sum(dictionary_test))


if __name__ == "__main__":
    main()
