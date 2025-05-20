# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# list 31:223
# delete
# pop = delete but retuns the deleted value


def main():
    list1 = [0, 1, 7, 3, 4, 5, 6]
    del list1[2]
    print("list1 is {}".format(list1))  # list1 is [0, 1, 3, 4, 5, 6]
    # same with pop
    list1 = [0, 1, 7, 3, 4, 5, 6]
    # similar to
    list2 = list1.pop(2)
    print("list1 is {}".format(list1))  # list1 is [0, 1, 3, 4, 5, 6]
    print("list2 is {}".format(list2))  # list2 is 7


if __name__ == "__main__":
    main()
