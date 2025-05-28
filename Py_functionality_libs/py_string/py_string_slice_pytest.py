#!/usr/bin/env python3
import os
import re
import pytest

TEST_STRING = "123_test"
DEFAULT_STEP = -2


def test_reversed_string():
    converted_string = TEST_STRING[::-1]
    checked_value = converted_string == "tset_321"
    print("Reversing string check is: {}".format(checked_value))
    assert checked_value


def test_reversed_string_with_step_in_variable():
    converted_string = TEST_STRING[::DEFAULT_STEP]
    checked_value = converted_string == "te_2"
    print("Reversing string check is with variable: {}".format(checked_value))
    assert checked_value


def test_reversed_string_with_step_in_variable_negative_assert():
    converted_string = TEST_STRING[::DEFAULT_STEP]
    checked_value = converted_string == "te_2"
    try:
        assert checked_value
        print("Reversing string negative assert is: {}".format(checked_value))
    except AssertionError as e:
        print("Reversing string negative assert is: {}".format(checked_value))


def main():
    test_string = "123foo.bar.two.three.two.two__com"
    # reversed string
    print(test_string[::-1])
    slice_variable = -1
    print(test_string[::slice_variable])
    test_reversed_string()
    test_reversed_string_with_step_in_variable()
    test_reversed_string_with_step_in_variable_negative_assert()


if __name__ == "__main__":
    main()
