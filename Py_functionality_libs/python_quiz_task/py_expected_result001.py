def func(val, lst=[]):
    lst.append(val)
    return lst


def main():
    print(func(1))
    print(func(2))
    print(func(3))
    assert func(4) == [1, 2, 3, 4]


if __name__ == "__main__":
    main()
