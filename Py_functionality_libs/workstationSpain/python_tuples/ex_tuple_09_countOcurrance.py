# https://pynative.com/python-tuple-exercise-with-solutions/

tuple1 = (50, 10, 60, 70, 50)


def count_occurances(test_tuple) -> list:
    return list(test_tuple).count(50)


def main():
    print(count_occurances(tuple1))
    try:
        assert 23 == count_occurances(tuple1)
    except AssertionError as ae:
        print("Wrong value: " + str(ae.__dict__))


if __name__ == "__main__":
    main()
