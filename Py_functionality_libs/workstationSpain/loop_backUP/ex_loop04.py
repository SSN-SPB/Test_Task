import pytest


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


def multiply_list(size_of_list, multiplier):
    return list(map(lambda x: x * multiplier, range(size_of_list)))


def main():
    print(multiply_list(10, 2))
    checking_result([0, 2, 4], multiply_list(3, 2), text="multiply the list")


def test_sum_of_array():
    assert multiply_list(10, 2) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


if __name__ == "__main__":
    main()
