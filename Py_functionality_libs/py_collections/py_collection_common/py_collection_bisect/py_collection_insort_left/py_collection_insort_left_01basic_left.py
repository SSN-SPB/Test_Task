# insort_left function inserts an element into a list in sorted order,
# maintaining the order of the list.
# It is part of the bisect module in Python.
# The function takes two arguments:
# the list to insert into
# and the value to insert.
# It finds the appropriate index to insert the value while
# keeping the list sorted and inserts it at that index.

from bisect import insort_left

tested_list = [10, 20, 70, 80, 100]


def main():
    insort_left(tested_list, 50)
    print(tested_list)


if __name__ == "__main__":
    main()
