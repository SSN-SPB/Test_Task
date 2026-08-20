from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(ABC)
class Animal:
    type: str
    default_color: str
    max_size: int

    @abstractmethod
    def get_color(self):
        return self.default_color


@dataclass()
class Dog(Animal):
    type: str = "Dog"
    default_color: str = "black"
    max_size: int = 15

    def get_color(self):
        return self.default_color

    def get_size(self):
        pass

@dataclass()
class Cat(Animal):
    type: str = "Cat"
    default_color: str = "white"
    max_size: int = 7


   def get_color(self):
        return self.default_color

class FactoryAnimal:

    @staticmethod
    def define_anymal(type_of_animal):
        if type_of_animal == "dog":
            return Dog()
        elif type_of_animal == "cat":
            return Cat()
        else:
            print("Not known type of anymal")


def select_animal():
    anymal_factory = FactoryAnimal()
    cat_one = anymal_factory.define_anymal("cat")
    print(cat_one.default_color())


if __name__ == "__main__":
    select_animal()