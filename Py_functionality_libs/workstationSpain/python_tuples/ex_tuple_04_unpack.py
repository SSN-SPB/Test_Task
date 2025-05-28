# https://pynative.com/python-tuple-exercise-with-solutions/

tuple1 = (10, 20, 30, 40)
tuple1 = (11, 20, 30, 40)
list1 = [11, 12, 13, 14]


def main():
    # unpack tuple into 4 variables
    a, b, c, d = tuple1
    a1, b1, c1, d1 = list1
    print(a)
    print(b)
    print(c)
    print(d)
    print(a1)
    print(b1)
    print(c1)
    print(d1)


if __name__ == "__main__":
    main()
