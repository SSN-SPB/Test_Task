# Builder Pattern is a creational design pattern that allows you to
# create complex objects step by step.
# It separates the construction of a complex object from its representation,
# allowing the same construction process to create different representations.
# Defines an interface for creating an object but lets
# subclasses alter the type of objects that will be created.
class CarBuilder:
    def __init__(self):
        self.car = {}

    def add_engine(self, engine):
        self.car["engine"] = engine
        return self

    def add_wheels(self, wheels):
        self.car["wheels"] = wheels
        return self

    def add_climate_control(self, climate_control):
        self.car["climate_control"] = climate_control
        return self

    def add_brand(self, brand):
        self.car["brand"] = brand
        return self

    def build(self):
        return self.car


def build_car_with_climate_control(engine, wheels, climate_control):
    return (
        CarBuilder()
        .add_engine(engine)
        .add_wheels(wheels)
        .add_climate_control(climate_control)
        .build()
    )


def build_car_tool():
    car = CarBuilder().add_engine("V8").add_wheels(4).add_brand("Ford").build()
    print(car)
    car1 = (
        CarBuilder().add_wheels(4).add_brand("Ford").add_engine("G8").build()
    )
    print(car1)
    car3 = build_car_with_climate_control(
        engine="V8", wheels=4, climate_control="separated_climate_control"
    )
    print(car3)


if __name__ == "__main__":
    build_car_tool()
