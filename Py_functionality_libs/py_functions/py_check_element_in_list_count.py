test_list = [10, 15, 20, 7, 46, 2808, "z", (1, 2)]
n = "15z"
n2 = (1, 2)


def main():
    print("Element {} is in lists: {}".format(n, bool(test_list.count(n))))
    print("Element {} is in lists: {}".format(n2, bool(test_list.count(n2))))


if __name__ == "__main__":
    main()
