#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1477/
# class 44:07
# parent classes
# super().__init__(xxx, yyy) takes __init__ of Parent


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def get_name(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def printname(self):
        print(self.firstname, self.lastname)


class Driver(Person):
    def __init__(self, fname, lname, car_model, car_mark):
        super().__init__(fname, lname)
        self.carmodel = car_model
        self.carmark = car_mark

    def print_car(self):
        print(self.carmodel, self.carmark)


def main2():
    x = Person("John", "Doe")
    x.printname()
    driver = Driver("Ivan", "Petrov", "Ford", "Focus")
    driver2 = Driver(x.get_name(), x.get_lastname(), "FW", "Polo")

    print(isinstance(x, Person))  # True
    print(isinstance(x, Driver))  # False
    print(isinstance(driver, Driver))  # True
    # the instance of child class is instance of Parent class as well
    print(isinstance(driver, Person))  # True
    print(Driver.__mro__)


if __name__ == "__main__":
    main2()
