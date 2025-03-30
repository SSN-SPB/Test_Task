def bubble_sort_early_stop(arr_stop):
    n = len(arr_stop)
    for i in range(n):
        swapped = False
        for j in range(0, n-1-i):
            if arr_stop[j] > arr_stop[j+1]:
                arr_stop[j], arr_stop[j+1] = arr_stop[j+1], arr_stop[j]
                swapped = True

        if not swapped:
            break
    return arr_stop

arr_stop = [6, 12, 18, 42, 94, 55, 44, 67]


def main2():
    c = Counter(19)
    # __doc__ displays the test message
    setattr(c, 'v4', 'hi')
    print(c.__dict__)
    print(getattr(c, 'v4'))  # hi
    c.get_value2()
    c.increase_value()
    c.get_value2()


if __name__ == '__main__':
    main2()
