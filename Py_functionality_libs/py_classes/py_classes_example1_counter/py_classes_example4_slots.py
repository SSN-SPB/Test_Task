#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1477/
# class 6:20
# __slots__  contains list of all possible attributes
# __slots__  consumes less memory because of it doesn't include __dict__


class Counter:
    """The class counts,increases and revealse some values"""

    __slots__ = ["value1", "value2", "value3"]

    def __init__(self, counter_value=0):
        self.value1 = 15
        self.value2 = counter_value
        self.value3 = "hello"

    def get_value1(self):
        # print(self.value)
        return self.value1

    def get_value2(self):
        # print(self.value)
        return self.value2

    def increase_value(self):
        self.value2 = self.value2 + 1
        return self.value2


def main2():
    c = Counter(19)
    try:
        print("c.__dict__ displays all " "attributes {}".format(c.__dict__))
    except AttributeError as ae:
        print("__dict__ is not found")
        print("ae is {}".format(ae))
    print("print 1st line with doc {}".format(c.__doc__))
    print("The list of attr: {}".format(Counter.__dict__))
    print("The value1 is: {}".format(c.get_value1()))
    print("The value2 is: {}".format(c.get_value2()))
    try:
        print("The value3 is: {}".format(c.get_value3()))
    except AttributeError as ae2:
        print("ae2 is {}".format(ae2))
    print("The default value3 is: {}".format(c.value3))


if __name__ == "__main__":
    main2()
