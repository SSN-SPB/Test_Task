# import collections

# any() and all() are built-in functions in Python
# that are used to check if any or all elements of
# an iterable (like a list, tuple, etc.) satisfy a certain condition.

tested_tuple = (0, 1, 2, 3, 4, 5)


def main():
    print(any(tested_tuple))
    print(all(tested_tuple))
    assert any(tested_tuple)
    assert not all(tested_tuple)


if __name__ == "__main__":
    main()
