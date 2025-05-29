def shift_right(init_list, shift_value):
    return init_list[-shift_value:] + init_list[:-shift_value]


def shift_left(init_list, shift_value):
    return init_list[shift_value:] + init_list[:shift_value]


def main():
    tested_list = list(range(0, 10))
    print(f"initial list: {tested_list}")  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    shifted_list_right = shift_right(tested_list, 3)
    shifted_list_left = shift_left(tested_list, 3)
    assert shifted_list_left == [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
    assert shifted_list_right == [7, 8, 9, 0, 1, 2, 3, 4, 5, 6]
    assert tested_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert tested_list[3:] == [3, 4, 5, 6, 7, 8, 9]
    assert tested_list[-3:] == [7, 8, 9]
    assert tested_list[-3::] == [7, 8, 9]
    assert tested_list[::-1] == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert tested_list[:-1] == [0, 1, 2, 3, 4, 5, 6, 7, 8]


if __name__ == "__main__":
    main()
