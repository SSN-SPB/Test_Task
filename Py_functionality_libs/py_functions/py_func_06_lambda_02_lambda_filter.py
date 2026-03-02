add_two = lambda x: x > 3
tested_list = list(range(0, 9))


def main():
    print(tested_list)
    # using lamda in map
    print(list(filter(add_two, tested_list)))
    assert list(filter(add_two, tested_list)) == [4, 5, 6, 7, 8]


if __name__ == "__main__":
    main()
