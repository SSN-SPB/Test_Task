# input data
list1 = [1, 2, 3, 4]
list2 = [21, 12, 13, 7, 15, 21]


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


def count_element_in_list(tested_list, element):
    return tested_list.count(element)


def main():
    checked_element = 3
    checking_result(
        1,
        count_element_in_list(list1, checked_element),
        "check element {} in list".format(checked_element),
    )


if __name__ == "__main__":
    main()
