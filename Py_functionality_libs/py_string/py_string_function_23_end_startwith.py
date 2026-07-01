# str.startswith
# str.endswith


string_test = "Hello $name! Welcome to $area!"


def main():
    assert string_test.startswith("Hello")
    print(f"Start with result: {string_test.startswith('Hello')}")
    try:
        assert string_test.endswith("Hello")
    except AssertionError as e:
        print(e.__doc__)
    assert string_test.endswith("$area!")
    print(f"Ends with result: {string_test.endswith('$area!')}")


if __name__ == "__main__":
    main()
