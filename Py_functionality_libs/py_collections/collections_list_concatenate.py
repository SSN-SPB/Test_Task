# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# list 20- 25
# concatenate += 26


def main():
    list1 = [0, 1]
    list2 = ['y1', 'y2']
    list1 += list2
    print(list1)      # [0, 1, 'y2', 'y1']
    list1 = []
    list2 = 'abcd'
    list1 += list2
    print(list1)      # ['a', 'b', 'c', 'd']


if __name__ == "__main__":
    main()
