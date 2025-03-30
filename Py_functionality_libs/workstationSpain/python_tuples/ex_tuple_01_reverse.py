# https://pynative.com/python-tuple-exercise-with-solutions/

tuple1 = (10, 20, 30, 40, 50)
expected_tuple = (50, 40, 30, 20, 11)


def reverse_tuple(test_tuple):
    interim_list = list(test_tuple)
    return tuple(interim_list[::-1])


def main():
    result_tuple = reverse_tuple(tuple1)
    print("Received: {}".format(result_tuple))
    try:
        assert result_tuple == expected_tuple, "Expected: " + str(expected_tuple)
    except AssertionError as ae4:
        print("Wrong value is received")
        print(ae4)


if __name__ == "__main__":
    main()
