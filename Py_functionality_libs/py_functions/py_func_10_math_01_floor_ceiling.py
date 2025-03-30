import py_math

value_one = 2.3


def main():
    assert py_math.floor(value_one) == 2
    assert py_math.ceil(value_one) == 3


if __name__ == "__main__":
    main()
