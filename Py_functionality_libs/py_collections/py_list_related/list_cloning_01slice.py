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


def cloning_list(tested_list):
    return tested_list


def main():
    checking_result(list1, cloning_list(list1), "checking cloned list")
    checking_result(list2, cloning_list(list2), "checking cloned list")


if __name__ == "__main__":
    main()
