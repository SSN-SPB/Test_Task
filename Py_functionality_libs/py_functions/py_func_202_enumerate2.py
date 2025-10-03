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


def enumerate_list_with_index(tested_list, enumerate_index):
    for index, element in enumerate(tested_list, start=enumerate_index):
        print(f"index: {index}, element: {element}")


def main():
    enumerate_list_with_index(test_list, 7)  # starting index - 7


if __name__ == "__main__":
    main()
