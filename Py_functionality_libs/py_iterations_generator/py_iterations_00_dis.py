# https://compscicenter.ru/courses/python/2015-autumn/classes/1542/
# 00:00
# iterations
import dis


tested_list = ['a', 'b', 'c']


def iterate_list(list):
    for x in list:
        print(x)


def main():
    iterate_list(tested_list)
    dis.dis("for x in tested_list:print(x)")
    # dis.dis("iterate_list(tested_list)")


if __name__ == "__main__":
    main()
