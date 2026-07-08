# input data
list1 = [1, 2, 3, 4]


def main():
    # 1 .insert(0, 6)
    list1.insert(0, 6)  # [6, 1, 2, 3, 4]
    print(list1)

    # list concatenation
    list3 = [7] + list1  # [7, 1, 2, 3, 4]
    print(list3)

    # list slicing
    list3 = [8] + list3[:]  # [8, 7, 6, 1, 2, 3, 4]
    print(list3)


if __name__ == "__main__":
    main()
