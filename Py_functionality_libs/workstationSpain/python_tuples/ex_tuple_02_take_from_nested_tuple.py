# https://pynative.com/python-tuple-exercise-with-solutions/

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
expected_value = 25


def main():
    for x in tuple1:
        print(type(x))
        if type(x) == tuple:
            print(x)
            for y in x:
                if y == 25:
                    print(y)


if __name__ == "__main__":
    main()
