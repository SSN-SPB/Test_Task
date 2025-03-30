# The @property decorator in Python is used to define
# a method that can be accessed like an attribute.
# It's often used to encapsulate data, providing a
# way to define getter, setter, and delete methods
# while maintaining a clean interface.
# with decorator @property
# print(f"Radius: {circle2.radius}")  # Accessing the radius using the property

# without decorator @property
# print(f"Radius: {circle.get_radius()}")  # Accessing the radius using the getter method


class Circle:
    def __init__(self, radius):
        self._radius = radius  # Use a protected variable to store the radius

    def get_radius(self):
        """Getter method for the radius."""
        return self._radius

    def set_radius(self, value):
        """Setter method for the radius with validation."""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    def get_area(self):
        """Method to calculate the area of the circle."""
        import math

        return math.pi * (self._radius**2)


# Using the Circle class
circle = Circle(5)
print(f"Radius: {circle.get_radius()}")  # Accessing the radius using the getter method
print(f"Area: {circle.get_area()}")  # Accessing the area using the method

circle.set_radius(10)  # Using the setter to update the radius
print(f"Updated Radius: {circle.get_radius()}")
print(f"Updated Area: {circle.get_area()}")

# Trying to set a negative radius will raise an exception
try:
    circle.set_radius(-5)
except ValueError as e:
    print(e)


# With decorator @property
class Circle2:
    def __init__(self, radius):
        self._radius = radius  # Use a protected variable to store the radius

    @property
    def radius(self):
        """Getter method for the radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter method for the radius with validation."""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        """Read-only property to calculate the area of the circle."""
        import math

        return math.pi * (self._radius**2)


# Using the Circle class
circle2 = Circle2(5)
print(f"Radius: {circle2.radius}")  # Accessing the radius using the property
print(f"Area: {circle2.area}")  # Accessing the area using the read-only property

circle2.radius = 10  # Using the setter to update the radius
print(f"Updated Radius: {circle2.radius}")
print(f"Updated Area: {circle2.area}")

# Trying to set a negative radius will raise an exception
try:
    circle2.radius = -5
except ValueError as e:
    print(e)
