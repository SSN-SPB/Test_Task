from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Animal(ABC):
    type: str
    default_color: str
    max_size: int

    @abstractmethod
    def get_color(self) -> str:
        pass


@dataclass()
class Dog(Animal):
    type: str = "Dog"
    default_color: str = "black"
    max_size: int = 15

    def get_color(self):
        return self.default_color

    def get_size(self):
        return self.max_size


@dataclass()
class Cat(Animal):
    type: str = "Cat"
    default_color: str = "white"
    max_size: int = 7

    def get_color(self):
        return self.default_color


class FactoryAnimal:

    @staticmethod
    def define_animal(type_of_animal):
        if type_of_animal == "dog":
            return Dog()
        elif type_of_animal == "cat":
            return Cat()
        else:
            print("Not known type of animal")


def select_animal():
    animal_factory = FactoryAnimal()
    animal_one = animal_factory.define_animal("cat")
    print(animal_one.type)
    print(animal_one.default_color)
    print(animal_one.get_color())
    assert animal_one.type == "Cat"

    animal_two = animal_factory.define_animal("dog")
    print(animal_two.type)
    print(animal_two.default_color)
    print(animal_two.get_color())
    assert animal_two.type == "Dog"


if __name__ == "__main__":
    select_animal()
