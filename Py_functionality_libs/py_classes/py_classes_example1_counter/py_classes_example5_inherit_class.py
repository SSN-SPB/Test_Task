#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1477/
# class 6:37
# parent classes


class Counter:
    """ The class counts,increases and revealse some values """
    __slots__ = ['value1', 'value2', 'value3']

    def __init__(self, counter_value=0):
        self.value1 = 15
        self.value2 = counter_value
        self.value3 = 'hello'

    def get_value1(self):
        # print(self.value)
        return self.value1

    def get_value2(self):
        # print(self.value)
        return self.value2

    def increase_value(self):
        self.value2 = self.value2 + 1
        return self.value2


class OtherCounter(Counter):
    """ The class inherits Counter class """

    def __init__(self, counter_value=5):
        self.value1 = 25
        self.value2 = counter_value
        self.value3 = 'hello other'


def main2():
    c = Counter(19)
    print('The value1 is: {}'.format(c.get_value1()))  # .. is: 15
    print('The value2 is: {}'.format(c.get_value2()))  # .. is: 19
    b = OtherCounter(77)
    # it uses the methods of the parent class
    print('The b value1 is: {}'.format(b.get_value1()))  # .. is: 25
    print('The b value2 is: {}'.format(b.get_value2()))  # .. is: 77
    print('b.value3 is {}'.format(b.value3))


if __name__ == '__main__':
    main2()
