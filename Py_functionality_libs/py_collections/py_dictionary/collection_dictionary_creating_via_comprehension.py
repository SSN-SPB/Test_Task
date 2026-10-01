# This code demonstrates how to create a dictionary
# using dictionary comprehension in Python.


def main():
    test_dictionary = {i: "A" + str(i) for i in range(7)}
    print(test_dictionary)


if __name__ == "__main__":
    main()
