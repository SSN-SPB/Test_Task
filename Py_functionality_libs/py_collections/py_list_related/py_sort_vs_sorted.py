# This code demonstrates the difference between the sort() method and the sorted() function in Python.
# The sort() method sorts a list in place and returns None,
# while the sorted() function returns a new sorted list without modifying the original list.

test_list_one = [10, 121, -7, 11]
test_list_two = [110, 1121, -17, 111]


def main():
    test_list_one.sort()
    print(f"test_list_one.sort():{test_list_one.sort()} - initial: {test_list_one}")
    print(f"sorted(test_list_two):{sorted(test_list_two)} - initial: {test_list_two}")
    sorted_test_list_two = sorted(test_list_two)
    print(f"sorted_test_list_two: {sorted_test_list_two} - initial: {test_list_two}")


if __name__ == "__main__":
    main()
