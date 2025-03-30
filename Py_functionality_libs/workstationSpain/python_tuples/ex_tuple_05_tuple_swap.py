# https://pynative.com/python-tuple-exercise-with-solutions/
tuple1 = (10, 20, 30, 40)
tuple2 = (11, 21, 31, 41)


def main():
    # tuple1 = (10, 20, 30, 40)
    # tuple2 = (11, 21, 31, 41)
    tuple1, tuple2 = tuple2, tuple1
    print(tuple1)
    print(tuple2)


if __name__ == "__main__":
    main()
