# Defines an interface for creating an object but lets
# subclasses alter the type of objects that will be created.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
        return None

# Usage
factory = AnimalFactory()
dog = factory.get_animal('dog')
cat = factory.get_animal('cat')
print(dog.speak())  # Woof!
print(cat.speak())  # Meow!
