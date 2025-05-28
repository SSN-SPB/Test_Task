#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1477/
# class 6:10
# method - function of class
# 1st method is constructor __init__(self, ...)
# constuctor returns nothing
# self - instance of class
# 6:10


class Counter:
    # all_found_values - an attribute of class
    all_found_values = []

    def __init__(self, counter_value=0):
        self.value2 = counter_value

    def get(self):
        # print(self.value)
        return self.value2

    def increase_value(self):
        self.value2 = self.value2 + 1
        return self.value2


def main():
    c = Counter(15)
    c.get()
    print("Initial value: {}".format(c.get()))
    c.increase_value()
    c.get()
    y = c.get()
    print("The assigned y is: {}".format(y))
    # working with an attribute of class
    c.all_found_values.append(2)  # [2]
    print(c.all_found_values)


if __name__ == "__main__":
    main()
