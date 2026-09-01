from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class BikeType(Enum):
    MOUNT = "mount_bike"
    CROSS = "cross_bike"
    RACE = "race_bike"


@dataclass()
class Bike(ABC):
    model: str
    type: str
    basic_speed: int

    @abstractmethod
    def get_speed(self):
        return self.basic_speed


@dataclass()
class MountainBike(Bike):
    model: str = "Honda"
    type: str = "mount_bike"
    basic_speed: int = 90

    def get_speed(self):
        return self.basic_speed * 1.2


@dataclass()
class RaceBike(Bike):
    model: str = "CZ"
    type: str = "race_bike"
    basic_speed: int = 120

    def get_speed(self):
        return self.basic_speed * 1.5


@dataclass()
class CrossBike(Bike):
    model: str = "Ural"
    type: str = "cross_bike"
    basic_speed: int = 90

    def get_speed(self):
        return self.basic_speed * 0.78


class FactoryBike:

    @staticmethod
    def get_bike_type(type_of_bike):
        if type_of_bike == BikeType.CROSS:
            return CrossBike()
        elif type_of_bike == BikeType.MOUNT:
            return MountainBike
        elif type_of_bike == BikeType.RACE:
            return MountainBike
        else:
            print("Type is not known")


def main():
    factory_of_bikes = FactoryBike()
    bike_one = factory_of_bikes.get_bike_type(BikeType.CROSS)
    print(f"speed of bike_one is {bike_one.get_speed()}")


if __name__ == "__main__":
    main()
