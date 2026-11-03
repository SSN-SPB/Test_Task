from enum import Enum


class Car(Enum):
    LORRY = 1
    SPORT = 2
    LUXURY = 3


def main():
    test_car = Car.LORRY
    print(f"index of Lorry car is: {test_car.value}")
    print(f"Name of Lorry car is: {test_car.name}")


if __name__ == "__main__":
    main()
