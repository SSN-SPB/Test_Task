from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract Base Class (ABC): The Animal class
    inherits from ABC, making it an abstract base class.
    Abstract Methods (@abstractmethod): Methods
    decorated with @abstractmethod must be implemented in any subclass.
    """

    @abstractmethod
    def make_sound(self):
        """Method that all subclasses must implement."""
        pass

    @abstractmethod
    def move(self):
        """Another method that all subclasses must implement."""
        pass


# Subclassing Animal and implementing the abstract methods
class Dog(Animal):
    def make_sound(self):
        return "Bark"

    def move(self):
        return "Runs on four legs"


class Bird(Animal):
    """Bird abstract of Animals"""
    def make_sound(self):
        """Bird chirps"""
        return "Chirp"

    def move(self):
        return "Flies in the sky"


class Human(Animal):
    def walk(self):
        return "Walks"

    def move(self):
        return "Runs"

    def make_sound(self):
        return "Says"


# Example usage
dog = Dog()
bird = Bird()
human = Human()

print(dog.make_sound())  # Output: Bark
print(dog.move())  # Output: Runs on four legs

print(bird.make_sound())  # Output: Chirp
print(bird.move())

print(human.make_sound())  # Output: Says
print(human.move())
print(human.walk())

print(human.__doc__)
print(Animal.__doc__)
print(bird.__doc__)
print(Bird.make_sound.__doc__)
