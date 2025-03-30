# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# set 43:00
# add('x') - one argument to set
# update('z', 'y') - one argument to set


def main():
    set1 = set()
    set2 = {0, 7, 2, 3, 7, 5, 6}
    print(set1)      # set()
    print(set2)      # {0, 2, 3, 5, 6, 7} 2nd '7' is removed without error

    set1.add('x')
    print(set1)      # {'x'}
    try:
        set1.add('z', 'y')
    except TypeError:
        print('only one element can be appended to set via .add')
    set1.update('z', 'y')
    print(set1)      # {'z', 'y', 'x'}


if __name__ == "__main__":
    main()
