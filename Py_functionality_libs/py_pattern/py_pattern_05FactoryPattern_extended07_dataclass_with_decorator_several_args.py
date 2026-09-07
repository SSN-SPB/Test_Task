from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Vegetable(ABC):
    name: str
    vegetable_type: str = "red"

    @abstractmethod
    def get_name(self) -> str:
        pass


@dataclass
class Cucumber(Vegetable):
    subtype: str = "long"
    basic_size = 15

    def get_name(self):
        return self.name + "_" + self.subtype

    def get_size(self):
        return self.basic_size


@dataclass
class Tomato(Vegetable):
    subtype: str = "pero"
    basic_size = 17

    def get_name(self):
        return self.name + "_" + self.subtype

    def get_size(self):
        return self.basic_size


class VegetableFactory:

    @staticmethod
    def select_vegetable(
        vegetable_type: str, name: str, subtype: str
    ) -> Vegetable:
        if vegetable_type == "green" and name == "cucumber":
            return Cucumber(
                vegetable_type=vegetable_type, name=name, subtype=subtype
            )

        if vegetable_type == "red" and name == "tomato":
            return Tomato(
                vegetable_type=vegetable_type, name=name, subtype=subtype
            )


def select_vegetables():
    factory_vegetable = VegetableFactory()
    vegetable_one = factory_vegetable.select_vegetable(
        vegetable_type="green", name="cucumber", subtype="short"
    )
    print(vegetable_one.get_name())
    print(vegetable_one.get_size())

    vegetable_two = factory_vegetable.select_vegetable(
        vegetable_type="red", name="tomato", subtype="ensalada"
    )
    print(vegetable_two.get_name())
    print(vegetable_two.get_size())


if __name__ == "__main__":
    select_vegetables()
