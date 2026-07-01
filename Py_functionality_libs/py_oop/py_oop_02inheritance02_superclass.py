# super() is a built-in function in Python that allows
# you to call methods from a parent class.
# It is commonly used in inheritance to access
# and extend the functionality of the parent class.


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent class constructor
        super().__init__(name)
        self.breed = breed

    def speak(self):
        # Call parent class method
        super().speak()
        print(f"{self.name} barks")


dog = Dog("Buddy", "Labrador")

print(dog.name)  # Buddy
print(dog.breed)  # Labrador

dog.speak()

# Output:
# Buddy
# Labrador
# Buddy makes a sound
# Buddy barks
