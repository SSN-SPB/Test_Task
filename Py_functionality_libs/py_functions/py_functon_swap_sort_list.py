def bubble_sort_early_stop(arr_stop):
    n = len(arr_stop)
    count1 = 0
    count2 = 0
    for i in range(n):
        swapped = False
        count1 += 1
        for j in range(0, n-1-i):
            if arr_stop[j] > arr_stop[j+1]:
                arr_stop[j], arr_stop[j+1] = arr_stop[j+1], arr_stop[j]
                swapped = True
            count2 += 1

        if not swapped:
            break
    print(count1)
    print(count2)
    return arr_stop


arr_stop = [6, 12, 18, 42, 94, 55, 44, 67]
arr_stop2 = [61, 12, 188, 142, 94, 55, 44, 67]


def main2():
    print(bubble_sort_early_stop(arr_stop))
    print(bubble_sort_early_stop(arr_stop2))


if __name__ == '__main__':
    main2()
