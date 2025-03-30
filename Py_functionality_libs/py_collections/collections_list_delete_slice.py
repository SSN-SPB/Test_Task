# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# list 31:22
# delete
# slice [:2] first 2;
# slice [::-1] list in the reverse order;
# slice [::2] each 2nd;
# slice [:] - all
# slice [a[start:stop:step]
# slice [:] - all
#  +---+---+---+---+---+---+
#   | P | y | t | h | o | n |
#   +---+---+---+---+---+---+
#   0   1   2   3   4   5   6
#  -6  -5  -4  -3  -2  -1


def main():
    list1 = [0, 1, 2, 3, 4, 5, 6]
    print(list1[:-1])  # [0, 1, 2, 3, 4, 5]
    print(list1[::-1]) # [6, 5, 4, 3, 2, 1, 0]
    del list1[:2]
    print(list1)      # [2, 3, 4, 5, 6]
    list1 = [0, 1, 2, 3, 4]
    # similar to
    del list1[0:2:1]
    print(list1)      # [2, 3, 4, 5, 6]
    list1 = [0, 1, 2, 3, 4, 5, 6]
    del list1[::2]
    print(list1)      # [1, 3, 5]
    list1 = [0, 1, 2, 3, 4, 5, 6]
    # similar to
    del list1[0:7:2]
    print(list1)      # [1, 3, 5]
    list1 = [0, 1, 2, 3, 4, 5, 6]
    del list1[:]
    print(list1)      # []
    list1 = [0, 1, 2, 3, 4, 5, 6]
    del list1[2:]
    print(list1)      # [0, 1]
    # similar to [2:7:1]
    list1 = [0, 1, 2, 3, 4, 5, 6]
    del list1[2:7:1]
    print(list1)      # [0, 1]


if __name__ == "__main__":
    main()
