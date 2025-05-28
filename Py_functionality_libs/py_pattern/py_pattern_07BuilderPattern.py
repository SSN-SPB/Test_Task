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

    def add_brand(self, brand):
        self.car["brand"] = brand
        return self

    def build(self):
        return self.car


car = CarBuilder().add_engine("V8").add_wheels(4).add_brand("Ford").build()
print(car)
car1 = CarBuilder().add_wheels(4).add_brand("Ford").add_engine("G8").build()
print(car1)
