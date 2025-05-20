test_list = [10, 1, 2, -3, 8, -5, 6, 7, 11, -2]


def bubble_sort_ascending(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list) - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print(my_list)


print("Sorted list in DESC order:", bubble_sort_ascending(test_list))
