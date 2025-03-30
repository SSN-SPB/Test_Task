# https://pynative.com/python-tuple-exercise-with-solutions/
tuple1 = (45, 45, 45, 46)


def check_if_item_the_same(test_tuple: "tuple") -> bool:
    return len(set(list(test_tuple))) == 1


def main():
    print(check_if_item_the_same(tuple1))


if __name__ == "__main__":
    main()

