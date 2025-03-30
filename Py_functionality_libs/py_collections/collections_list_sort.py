# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# list 33:07
# reverse
# returns nothing


def main():
    list1 = [0, 7, 2, 3, 4, 5, 6]
    list1.sort()
    print(list1)      # [0, 2, 3, 4, 5, 6, 7]
    list2 = [0, 7, 2, 3, 4, 5, 6]
    list2.sort(reverse=True)
    print(list2)      # [7, 6, 5, 4, 3, 2, 0]
    list3 = [0, 7, 2, 3, 4, 5, 6]
    list3.sort(key=lambda x: x % 3, reverse=True)
    print(list3)      # [2, 5, 7, 4, 0, 3, 6]
    print(2 % 3)      # 2
    print(5 % 3)      # 2
    print(7 % 3)      # 1
    print(4 % 3)      # 1
    print(0 % 3)      # 0
    print(3 % 3)      # 0
    print(6 % 3)      # 0


if __name__ == "__main__":
    main()
