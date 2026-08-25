import pytest

STRING_TEST = "bbbbb"


@pytest.mark.parametrize(
    "string_to_test, expected_length",
    [
        ("bbbb", 4),
        ("bbbb1", 1),
        ("bbbb2", 5),
        ("bbbb3", 5),
        ("bbbbc", 5),
    ],
)
def test_longest_substring(string_to_test, expected_length):
    assert len(string_to_test) == expected_length


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
