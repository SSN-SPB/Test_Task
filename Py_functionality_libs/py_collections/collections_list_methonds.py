#!/usr/bin/env python3

def compare_lists(list_a, list_b):
    print(list_a.__dir__)
    print(list_b.__dir__)
    print('hash of list is {}'.format(list_a.__hash__))
    print('hash of list is {}'.format(list_a.__hash__))
    print('lists are equals {}'.format(list_a == list_b))
    print('lists are the same object {}'.format(list_a is list_b))    


def main2():
    print('list of list\'s methonds')
    for x in dir(list):
        print('attributes of list {}'.format(x))
    list1 = [1, 'a', True]
    list2 = list1.copy()
    compare_lists(list1, list2)
    list3 = list1
    compare_lists(list1, list3)
    list1[0] = 2
    print(list1)
    print(list2)
    print(list3)
          

if __name__ == '__main__':
    main2()
