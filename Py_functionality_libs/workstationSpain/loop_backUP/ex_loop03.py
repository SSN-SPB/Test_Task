import pytest

def checking_result(expected, received, text="Check maximal val"):
    print(text)
    print('expected: {}'.format(expected))
    print('received: {}'.format(received))
    try:
        assert expected == received
        print('Checking has passed')
    except AssertionError as ae:
        print("checking has failed. \n__doc__: {}".format(ae.__doc__))
        print("__context__: {}".format(ae.__context__))


def create_sum(init_sum, x):
    return init_sum + x


def calculate_sum_of_range(maximal_in_range):
    result = 0
    for x in range(0, maximal_in_range + 1):
        result = create_sum(result, x)
    return result


def main():
    print(calculate_sum_of_range(10))
    checking_result(55, calculate_sum_of_range(10), text="Check sum of range")



def test_sum_of_array():
    assert calculate_sum_of_range(10) == 55


if __name__ == "__main__":
    main()