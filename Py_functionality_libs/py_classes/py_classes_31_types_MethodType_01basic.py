# MethodType is a function that allows you to bind a
# function to an instance of a class.
# This is useful when you want to add a method
# to an instance of a class at runtime.
from types import MethodType


class ClassCar:
    def __init__(self, speed):
        self.speed = speed

    def __str__(self):
        return f"ClassCar(speed={self.speed})"

    def display_current_speed(self):
        return self.speed


def increase_speed(self, increment):
    self.speed += increment
    return self.speed


def car_treating():
    car_one = ClassCar(7)
    car_one.speed_increase = MethodType(increase_speed, car_one)
    print(car_one.speed_increase(5))
    print(car_one.speed_increase(13))
    print(car_one.speed_increase(23))
    print(car_one)
    print(car_one.display_current_speed())
    assert car_one.speed_increase(13) == 61


if __name__ == "__main__":
    car_treating()
