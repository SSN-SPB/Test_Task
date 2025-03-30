# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# list 31:22
# delete
# slice [:2] first 2;
# slice [::-1] list in the reverse order;
# slice [::2] each 2nd;
# slice [:] - all
# slice [a[start:stop:step]
#  +---+---+---+---+---+---+
#   | P | y | t | h | o | n |
#   +---+---+---+---+---+---+
#   0   1   2   3   4   5   6
#  -6  -5  -4  -3  -2  -1


def main():
    list1 = [0, 1, 2, 3, 4, 5, 6]
    list1.reverse()
    print('list after reverse() {}'.format(list1))
    # [6, 5, 4, 3, 2, 1, 0]
    list2 = list1[::-1]
    print('list after [::-1] {}'.format(list2))
    print(list2[:-1])   # [0, 1, 2, 3, 4, 5]
    print(list2[::-1])  # [6, 5, 4, 3, 2, 1, 0]
    del list1[:2]
    print(list1)        # [4, 3, 2, 1, 0]


if __name__ == "__main__":
    main()
