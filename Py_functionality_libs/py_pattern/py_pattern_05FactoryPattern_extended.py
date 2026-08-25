class FordCar:

    def __init__(self, model, base_price):
        self.model = model
        self.base_price = base_price

    def get_base_price(self):
        return self.price


class FordMondeo(FordCar):

    def __init__(self):
        super().__init__("Mondeo", 100)

    def get_base_price(self):
        return self.base_price * 2

    def get_model(self):
        return self.model


class FordTaurus(FordCar):

    def __init__(self):
        super().__init__("Taurus", 130)

    def get_base_price(self):
        return self.base_price * 3

    def get_model(self):
        return self.model


class FordMustang(FordCar):

    def __init__(self):
        super().__init__("Mustang", 300)

    def get_base_price(self):
        return self.base_price * 5

    def get_model(self):
        return self.model


class FordFactory:

    @staticmethod
    def define_model(selected_model):
        if selected_model == "Mustang":
            return FordMustang()
        if selected_model == "Taurus":
            return FordTaurus()
        if selected_model == "Mondeo":
            return FordMondeo()


def main():
    ford_factory = FordFactory()

    car_one = ford_factory.define_model("Mustang")
    print(car_one.get_base_price())
    print(car_one.get_model())

    car_two = ford_factory.define_model("Mondeo")
    print(car_two.get_base_price())
    print(car_two.get_model())

    car_three = ford_factory.define_model("Mustang")
    print(car_three.get_base_price())
    print(car_three.get_model())


if __name__ == "__main__":
    main()
