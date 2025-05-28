import pytest

numbers = [12, 75, 150, 180, 145, 525, 50]


def checking_result(expected, received, text="Check maximal val"):
    print(text)
    print("expected: {}".format(expected))
    print("received: {}".format(received))
    try:
        assert expected == received
        print("Checking has passed")
    except AssertionError as ae:
        print("checking has failed. \n__doc__: {}".format(ae.__doc__))
        print("__context__: {}".format(ae.__context__))


def create_sum(init_sum, x):
    return init_sum + x


def list_checking(tested_list):
    result_list = []
    for x in tested_list:
        if isinstance(x, int) and x > 500:
            break
        elif isinstance(x, int) and x % 5 != 0:
            continue
        elif isinstance(x, int) and x > 150:
            continue
        if isinstance(x, int):
            result_list.append(x)

    return result_list


def main():
    checking_result([75, 150, 145], list_checking(numbers), text="check the list")


def test_sum_of_array():
    assert list_checking(numbers) == [75, 150, 145]


if __name__ == "__main__":
    main()
