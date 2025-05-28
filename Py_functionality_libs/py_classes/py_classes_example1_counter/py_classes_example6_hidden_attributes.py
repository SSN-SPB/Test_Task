#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1477/
# class 7:10
# all_found_values - an attribute of class
# _all_reserved_values - an hidden attribute of class
# __all_active_values - an double hidden attribute of class


class Counter:
    # all_found_values - an attribute of class
    all_found_values = []
    _all_reserved_values = []
    __all_active_values = []

    def __init__(self, counter_value=0):
        self.value2 = counter_value


def main():
    c = Counter(15)
    # working with an attribute of class
    c.all_found_values.append(2)  # [2]
    print(c.all_found_values)
    x = Counter._all_reserved_values
    x.append("z")
    print(x)  # [z]
    print(c._all_reserved_values)  # [z]
    Counter._Counter__all_active_values.append(-1)
    # The special call of double hidden attributes of class
    print(Counter._Counter__all_active_values)  # [-1]


if __name__ == "__main__":
    main()
