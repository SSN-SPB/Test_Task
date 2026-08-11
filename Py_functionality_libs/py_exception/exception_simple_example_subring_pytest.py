STRING_TEST = "bbbbb"


def longest_substring(string_to_test):
    result = 1
    return result


def main():
    print(longest_substring(STRING_TEST))
    try:
        assert longest_substring(STRING_TEST) == 2
    except AssertionError as ae:
        print("checking has failed")
        print(ae.__context__)
        print(ae.__doc__)
        print(ae.__class__)
        print(ae.args)


if __name__ == "__main__":
    main()