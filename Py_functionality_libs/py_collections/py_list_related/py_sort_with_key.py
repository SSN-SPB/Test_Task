# This code demonstrates the difference between the sort() method
# and the sorted() function in Python.
# The sort() method sorts a list in place and returns None,
# while the sorted() function returns a new sorted list
# without modifying the original list.
# Additionally, it shows how to use a custom sorting key to sort a list
# of strings based on their length in reverse order.

list_one = [10, 121, -7, 11]
list_two = [110, 1121, -17, 111]
list_strings = ["apple", "banana", "egg", "cherry", "date", "elderberry"]


def sort_key_as_len(x):
    return len(str(x))


def main():
    list_one.sort()
    print(f"list_one.sort():{list_one.sort()} - initial: {list_one}")
    print(f"sorted(list_two):{sorted(list_two)} - initial: {list_two}")
    sorted_list_two = sorted(list_two)
    print(f"sorted_list_two: {sorted_list_two} - initial: {list_two}")
    print(
        f"sorted(list_):{sorted(list_strings, key=sort_key_as_len, reverse=True)} - initial: {list_strings}"
    )
    print(
        f"list_.sort():{list_strings.sort(key=sort_key_as_len, reverse=True)} - modified initial: {list_strings}"
    )


if __name__ == "__main__":
    main()
