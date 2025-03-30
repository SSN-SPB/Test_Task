# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# set 43:00
# add('x') - one argument to set
# update('z', 'y') - one argument to set


def main():
    set1 = set()
    set2 = {0, 7, 2, 3, 7, 5, 6}
    set3 = {'0x', '7x', '2x', '7x', '5x', 6}
    set4 = set.union(set1, set2, set3)
    print(set1)      # set()
    print(set2)      # {0, 2, 3, 5, 6, 7} 2nd '7' is removed without error

    print('set3 is {}'.format(set3))
    # set3 is {6, '2x', '5x', '7x', '0x'}
    print('set4 is {}'.format(set4))
    # set4 is {0, 2, 3, 5, 6, 7, '2x', '5x', '7x', '0x'}

    set5 = set.intersection(set2, set3)
    print('set5 is {}'.format(set5))     # {6}
    set6 = set.difference(set2, set3)
    print('set6 is {}'.format(set6))     # set6 is {0, 2, 3, 5, 7}
    set7 = set.difference(set3, set2)
    # set3 - set2
    print('set7: {}'.format(set7))         # set7: {'7x', '2x', '5x', '0x'}
    print('set8: {}'.format(set3 - set2))  # set8: {'7x', '2x', '5x', '0x'}


if __name__ == "__main__":
    main()
