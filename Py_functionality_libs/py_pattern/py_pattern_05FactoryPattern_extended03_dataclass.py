from dataclasses import dataclass


@dataclass()
class Ship:
    type: str
    model: str
    speed: int

    def get_speed(self):
        return self.speed


class River(Ship):
    def __init__(self):
        super().__init__(type="River", model="sandCarrier", speed=100)

    def get_speed(self):
        return self.speed - 10


class Sea(Ship):
    def __init__(self):
        super().__init__(type="Sea", model="grainCarrier", speed=90)

    def get_speed(self):
        return self.speed - 15


class ShipFactory:

    @staticmethod
    def define_ship_type(type_of_ship):
        if type_of_ship == "sea":
            return Sea()
        elif type_of_ship == "river":
            return River()
        else:
            print("It is not known type")


def defineShip():
    factory = ShipFactory()
    ship_one = factory.define_ship_type("sea")
    print(ship_one.get_speed())
    ship_two = factory.define_ship_type("river")
    print(ship_two.get_speed())
    ship_three = factory.define_ship_type("lake")


if __name__ == "__main__":
    defineShip()
