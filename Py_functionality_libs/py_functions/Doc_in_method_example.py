# Ascending Order: Sorts by always moving larger elements to the end
test_list = [10, 1, 2, 3, 8, 5, 6, 7, 11, -2]


def swap(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]


def bubble_sort_ascending(arr):
    """
    Ascending Order: Sorts by always moving larger elements to the end.

    Parameters:
    arr (list): The list to be sorted

    Returns:
    arr: sorted array.
    """
    for itm in arr:
        for idx in range(len(arr) - 1):
            if arr[idx] > arr[idx + 1]:
                swap(arr, idx, idx + 1)
    return arr


print("Sorted list in ASC order:", bubble_sort_ascending(test_list))
print(bubble_sort_ascending.__doc__)