def swap_positions(tested_list, pos1, pos2):
    tested_list[pos1], tested_list[pos2] = tested_list[pos2], tested_list[pos1]


newList = [12, 35, 9, 56, 25]


def main():
    swap_positions(newList, 0, 1)
    print(newList)


if __name__ == "__main__":
    main()
