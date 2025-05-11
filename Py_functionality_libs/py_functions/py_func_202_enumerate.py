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
    for i, e in enumerate(test_list):
        print("index: {}, element: {}".format(i, e))
        test_dict[i] = e
    print(test_dict)
    enumerate_list(test_list)


if __name__ == "__main__":
    main()
