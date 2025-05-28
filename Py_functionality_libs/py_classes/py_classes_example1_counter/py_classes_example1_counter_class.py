#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1477/
# class
# method - function of class
# 1st method is constructor __init__(self, ...)
# self - instance of class


class Counter:
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


if __name__ == "__main__":
    main()
