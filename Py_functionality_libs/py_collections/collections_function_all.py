# all check if all elements in collection are True


def main():
    print(all([0, 1, 2, 3, 4, 5, 6]))
    print(all([10, 1, 2, 3, -4, 5, 6]))
    assert all((2, "x")) is True
    assert all({2: "two", 1: "x"}) is True
    assert all({2: "two", 0: "x"}) is not True


if __name__ == "__main__":
    main()
