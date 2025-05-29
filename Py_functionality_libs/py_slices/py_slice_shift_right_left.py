def shift_right(init_list, shift_value):
    return init_list[-shift_value:] + init_list[:-shift_value]


def shift_left(init_list, shift_value):
    return init_list[shift_value:] + init_list[:shift_value]


def main():
    tested_list = list(range(0, 10))
    print(f"initial list: {tested_list}")
    modified_list_right = shift_right(tested_list, 3)
    modified_list_left = shift_left(tested_list, 3)
    print(f"shifted list left: {modified_list_left}")
    print(f"shifted list right: {modified_list_right}")
    print(f"initial list: {tested_list}")
    print(f"initial list part 1: {tested_list[3:]}")
    print(f"initial list part 2: {tested_list[-3:]}")
    print(f"initial list part 3: {tested_list[-3::]}")
    print(f"initial list part 4: {tested_list[::-1]}")
    print(f"initial list part 5: {tested_list[:-1]}")


if __name__ == "__main__":
    main()
