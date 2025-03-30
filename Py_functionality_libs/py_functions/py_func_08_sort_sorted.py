my_list1 = [1, 5, 8, 2, 15, 3]
my_list2 = [11, 51, 81, 21, 151, 31]


def main():
    print(type(my_list1.sort()))  # <class 'NoneType'>
    print(my_list1)  # not modified initial list
    print(type(sorted(my_list2)))  # <class 'list'>
    print(my_list2)  # not modified initial list
    assert my_list1 == [1, 2, 3, 5, 8, 15]
    assert my_list2 == [11, 51, 81, 21, 151, 31]


if __name__ == "__main__":
    main()
