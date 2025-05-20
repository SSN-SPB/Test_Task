tested_list = [12, 35, 9, 56, 25]


def main():
    print(tested_list)
    sorted(tested_list)
    print(tested_list)
    assert tested_list == [12, 35, 9, 56, 25]
    tested_list.sort()
    print(tested_list)
    assert tested_list == [9, 12, 25, 35, 56]


if __name__ == "__main__":
    main()
