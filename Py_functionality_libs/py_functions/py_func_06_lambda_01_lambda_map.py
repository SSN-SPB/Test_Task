add_two = lambda x: x + 2
tested_list = list(range(0, 9))


def main():
    print(tested_list)
    # using lamda in map
    print(list(map(add_two, tested_list)))
    print(map(add_two, tested_list))


if __name__ == "__main__":
    main()
