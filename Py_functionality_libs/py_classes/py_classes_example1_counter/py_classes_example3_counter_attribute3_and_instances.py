# !/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1477/
# class 6:14
# __doc__  contains 1st line message (if it exists)
# __class__.__name__ name of class of instance
# __dict__ dict of exemplar or class
# constuctor returns nothing
# self - instance of class
# 6:10
import inspect


class Counter:
    """The class counts,increases and revealse the values"""

    # all_found_values = []

    def __init__(self, counter_value=0):
        self.value2 = counter_value

    def get(self):
        # print(self.value)
        return self.value2

    def increase_value(self):
        self.value2 = self.value2 + 1
        return self.value2


def print_arguments(customer_dict):
    for k, v in customer_dict:
        print("argument is : {} has value {}".format(k, v))


def main2():
    c = Counter(15)
    zz = Counter(125)
    print("the dir of exemplar is {}".format(dir(c)))
    print("the dir of class is {}".format(dir(Counter)))
    # c.get()
    print("c.__dict__ displays all " "attributes of exemplar: {}".format(c.__dict__))
    print("Initial value: {}".format(c.get()))
    c.increase_value()
    print("New spead of c is: {}".format(c.get()))
    # __doc__ prints the 1st line of class
    print("c.__doc__ is: {}".format(c.__doc__))
    print("c.__init__ has type: {}".format(type(c.__init__)))
    print("c.__init__ has methods: {}".format(c.__init__.__dict__))
    for x in inspect.getmembers(c.__init__.__dict__):
        print("getmember: {}".format(x))
    print("c.__init__ getmembers: {}".format(dir(c.__init__)))

    print("__class__.__name__ is: {}".format(c.__class__.__name__))  # Counter
    s = "hello"
    print(s.__class__.__name__)  # str
    print(Counter.__module__)  # __main__
    print(c.__dict__)  # {'value2': 16}
    print(Counter.__dict__)  # {'__module__': '__main__', '__doc__': '...
    print_arguments(c.__dict__.items())
    print_arguments(Counter.__dict__.items())


if __name__ == "__main__":
    main2()
