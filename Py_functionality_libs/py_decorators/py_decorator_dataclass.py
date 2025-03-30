from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    model: str
    produced: int
    speed: 0

    def increase_speed(self, added_speed: int):
        self.speed += added_speed


def print_car():
    print(Car(brand="Ford1", model="1", produced=3, speed=5))
    car = Car(brand="Ford", model="", produced=1, speed=2)
    car.model = "Focus"
    car.produced = 2017
    print(car)
    print(car.produced)
    car.increase_speed(17)
    print(car.speed)

    set_of_values = {"brand": "Hundai", "model": "Gets",
                     "produced": 199, "speed": 112}
    car2 = Car(**set_of_values)
    print(car2.speed)


if __name__ == "__main__":
    print_car()
