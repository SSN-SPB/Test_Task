# __author__ = "Your Name"
# __date__ = "2024-06-10"
# format() is a built-in function that allows you to format an object
# using a specific format specification.
# this script demonstrates how to implement the __format__ method
# in a class to customize its string representation based on
# the format specification provided.

from abc import ABC, abstractmethod


class Car(ABC):

    def __init__(self, speed):
        self.speed = speed

    @abstractmethod
    def get_max_speed(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Lorry(Car):
    def __init__(self, load, speed):
        self.load = load
        super().__init__(speed)

    def get_max_speed(self):
        return self.speed

    def __repr__(self):
        return f"{self.__class__} with {self.__dict__}"

    def __format__(self, format_spec):
        if format_spec == "short":
            return (
                f"{self.__class__} with {self.__dict__}"
                f" and speed: {self.speed}. The size is {self.__sizeof__()}"
            )
        return f"{self.__doc__} with {self.__dict__}"


def main():
    car_one = Lorry(55, 11)
    print(car_one.get_max_speed())
    print(format(car_one, "short"))


if __name__ == "__main__":
    main()
