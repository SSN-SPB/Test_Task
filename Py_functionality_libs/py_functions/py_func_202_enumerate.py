test_list = [1, 5, 7, 9, 10, 11]
test_dict = dict()


def main():
    for i, e in enumerate(test_list):
        print("index: {}, element: {}".format(i, e))
        test_dict[i] = e
    print(test_dict)


if __name__ == "__main__":
    main()
