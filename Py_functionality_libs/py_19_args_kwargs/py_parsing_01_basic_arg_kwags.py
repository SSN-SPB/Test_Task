def display_arguments(a, *args, **kwargs):
    print(f"a is {a},\nargs are {args},\nkwargs are {kwargs}")
    return a, args, kwargs


def main():
    a1, arg1, kwarg1 = display_arguments(7, "a", "b", "c", key="k1", value="v1")
    assert a1 == 7
    assert arg1 == ("a", "b", "c")
    assert kwarg1 == {"key": "k1", "value": "v1"}
    assert str(type(arg1)).count("tuple") == 1
    assert str(type(kwarg1)).count("dict") == 1


if __name__ == "__main__":
    main()
