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
        return f"{self.__class__} with {self.__dict__}"


def main():
    car_one = Lorry(55, 11)
    print(car_one.get_max_speed())
    print(repr(car_one))


if __name__ == "__main__":
    main()
