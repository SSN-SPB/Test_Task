def bubble_sort_early_stop(arr_stop):
    count1, count2 = 0, 0
    n = len(arr_stop)
    for i in range(n):
        count1 += 1
        swapped = False
        for j in range(0, n - 1 - i):
            count2 += 1
            if arr_stop[j] > arr_stop[j + 1]:
                arr_stop[j], arr_stop[j + 1] = arr_stop[j + 1], arr_stop[j]
                swapped = True
        if not swapped:
            break
    print(count1)
    print(count2)
    return arr_stop


test_array = [6, 12, 18, 42, 94, 55, 44, 67]
test_array_sorted = [6, 12, 18, 42, 44, 55, 67, 94]

print("Ascending with Early Stopping:", bubble_sort_early_stop(test_array))
print("Sorted with Early Stopping:", bubble_sort_early_stop(test_array_sorted))
