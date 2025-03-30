#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1477/
# class 40:37
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
    driver = Driver('Ivan', 'Petrov', 'Ford', 'Focus')
    driver.printname()
    driver.print_car()
    driver2 = Driver(x.get_name(), x.get_lastname(), 'FW', 'Polo')
    driver2.printname()
    driver2.print_car()


if __name__ == '__main__':
    main2()
