test_list = [
    "10a",
    "11a",
    "12a",
    "13a",
    "14a",
    "15a",
    "16a",
]
test_dict = dict()


def enumerate_list(tested_list):
    for index, element in enumerate(tested_list):
        print(f"index: {index}, element: {element}")


def main():
    enumerate_list(test_list)
    for i, e in enumerate(test_list):
        print("Adding to dictionary index: {}, element: {}".format(i, e))
        test_dict[i] = e
    print(f"Modified dictionary: {test_dict}")


if __name__ == "__main__":
    main()
