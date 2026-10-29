# insort_left function inserts an element into a list in sorted order,
# maintaining the order of the list.
# It is part of the bisect module in Python.
# The function takes two arguments:
# the list to insert into
# and the value to insert.
# It finds the appropriate index to insert the value while
# keeping the list sorted and inserts it at that index.

# if the list is not sorted, the function will still
# insert the value at the appropriate index,
# but the list will not be sorted after the insertion.

# in takes the value of element with middle index of the list
# and compares it with the value to be inserted.
# if the value to be inserted is less than the middle element,
# function takes the left half of the list and repeats the process
# from the middle of the left half. E.g. for indexes 0 to 10,
# the middle index is 5,
# then the left half is indexes 0 to 5,
# and the middle index of that is 2, and so on.


from bisect import insort_left

tested_list = [110, 10, 70, 20, 60, 70, 80, 100]
tested_list3 = [110, 10, 70, 20, 60, 70, 80, 100, 10, 70]
tested_list5 = [110, 1, 3, 10, 70, 93, 90, 60, 70, 80, 100, 10, 70]


def main():
    insort_left(tested_list, 63)
    print(tested_list)
    insort_left(tested_list3, 63)
    print(tested_list3)
    insort_left(tested_list5, 63)
    print(tested_list5)
    assert [110, 10, 70, 20, 60, 63, 70, 80, 100] == tested_list
    assert [110, 10, 63, 70, 20, 60, 70, 80, 100, 10, 70] == tested_list3
    assert [
        110,
        1,
        3,
        10,
        63,
        70,
        93,
        90,
        60,
        70,
        80,
        100,
        10,
        70,
    ] == tested_list5


if __name__ == "__main__":
    main()
