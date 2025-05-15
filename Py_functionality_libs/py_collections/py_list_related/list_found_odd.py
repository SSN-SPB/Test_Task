# input data
list1 = [1, 2, 3, 4]
list2 = [11, 12, 13, 14, 15]


def checking_result(
    expected, received, text="Compare the expected" "and the received result"
):
    print(text)
    print("expected: {}".format(expected))
    print("received: {}".format(received))
    try:
        assert expected == received
        print("Checking has passed")
    except AssertionError as ae:
        print("checking has failed. \n__doc__: {}".format(ae.__doc__))
        print("__context__: {}".format(ae.__context__))


def found_even_in_list(tested_list):
    result_list = []
    for x in tested_list:
        if x % 2 != 0:
            result_list.append(x)
    return result_list


def main():
    checking_result([1, 3], found_even_in_list(list1), "checking odd in list")
    checking_result([2, 4], found_even_in_list(list2), "checking even in list")


if __name__ == "__main__":
    main()
