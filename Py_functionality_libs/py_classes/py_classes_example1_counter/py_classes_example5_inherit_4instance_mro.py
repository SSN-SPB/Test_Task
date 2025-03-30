#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1477/
# class 51:07
# parent classes
# __mro__ Main Resolution Order - order of treating class hierarchy

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


class Driver_Taxi(Driver):
    def __init__(self, fname, lname, car_model, car_mark, taxi_company):
        super().__init__(fname, lname, car_model, car_mark)
        self.taxi_company = taxi_company

    def print_car(self):
        print(self.carmodel, self.carmark)

    def print_car_park(self):
        print(self.taxi_company)


def main2():
    x = Person("John", "Doe")
    print(Driver.__mro__)
    # (<class '__main__.Driver'>, <class '__main__.Person'>, <class 'object'>)
    print(Person.__mro__)
    print(Driver_Taxi.__mro__)
    y = Driver_Taxi("John", "Doe", 'Ford', 'Focus', 'Yandex')
    y.print_car()
    y.print_car_park()


if __name__ == '__main__':
    main2()
