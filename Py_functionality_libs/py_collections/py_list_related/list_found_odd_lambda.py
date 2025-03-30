# input data
list1 = [1, 2, 3, 4]
list2 = [21, 12, 13, 7, 15, 21]


def checking_result(expected, received, text="Compare the expected"
                                             "and the received result"):
    print(text)
    print('expected: {}'.format(expected))
    print('received: {}'.format(received))
    try:
        assert expected == received
        print('Checking has passed')
    except AssertionError as ae:
        print("checking has failed. \n__doc__: {}".format(ae.__doc__))
        print("__context__: {}".format(ae.__context__))


def cloning_list(tested_list):
    result_list = []
    for v in tested_list:
        result_list.append(v) if v % 2 != 0 else print('not odd')
    return sorted(result_list)


def main():
    checking_result([1, 3], found_even_in_list(list1), 'checking odd in list')
    checking_result([2, 4], found_even_in_list(list2), 'checking even in list')


if __name__ == "__main__":
    main()
