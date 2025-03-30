"""The @dataclass decorator, available in the dataclasses module,
simplifies the creation of classes by automatically generating common methods
 such as __init__, __repr__, and __eq__"""

from dataclasses import dataclass


# without decorator @dataclass
class Park:

    def __init__(self, city, park_name, park_size):
        self.city = city
        self.park_name = park_name
        self.park_size = park_size

    def __repr__(self) -> str:
        return f"Park attribute(city = {self.city}, park_name = {self.park_name}, park_size = {self.park_size})"

    def __eq__(self, other):
        if isinstance(other, Park):
            return (
                other.park_size == self.park_size
                and other.park_name == self.park_name
                and other.city == self.city
            )
        return False


park_one = Park("SPB", "Letniy", 20)
park_three = Park("SPB", "Letniy", 20)
park_two = Park("MSC", "Alexandrovsky", 10)

print(park_one == park_two)
print(park_one == park_three)
print(park_three)


@dataclass
class Park2:
    city: str
    park_name: str
    park_size: int

    def __repr__(self) -> str:
        return f"Park2 attribute(city = {self.city}, park_name = {self.park_name}, park_size = {self.park_size})"

    def __eq__(self, other):
        if isinstance(other, Park2):
            return (
                other.park_size == self.park_size
                and other.park_name == self.park_name
                and other.city == self.city
            )
        return False


park_one = Park2("SPB", "Letniy", 20)
park_three = Park2("SPB", "Letniy", 20)
park_two = Park2("MSC", "Alexandrovsky", 10)

print(park_one == park_two)
print(park_one == park_three)
print(park_three)

# class TestResult:
#     def __init__(self, test_name, status, duration):
#         self.test_name = test_name
#         self.status = status
#         self.duration = duration
#
#     def __repr__(self):
#         return f"TestResult(test_name={self.test_name}, status={self.status}, duration={self.duration})"
#
#     def __eq__(self, other):
#         if isinstance(other, TestResult):
#             return (self.test_name == other.test_name and
#                     self.status == other.status and
#                     self.duration == other.duration)
#         return False
#
# result1 = TestResult("TestLogin", "Passed", 5.23)
# result2 = TestResult("TestLogin", "Passed", 5.23)
#
# print(result1)  # Output: TestResult(test_name=TestLogin, status=Passed, duration=5.23)
# print(result1 == result2)  # Output: True


# class Circle:
#     def __init__(self, radius):
#         self._radius = radius  # Use a protected variable to store the radius
#
#     def get_radius(self):
#         """Getter method for the radius."""
#         return self._radius
#
#     def set_radius(self, value):
#         """Setter method for the radius with validation."""
#         if value < 0:
#             raise ValueError("Radius cannot be negative")
#         self._radius = value
#
#     def get_area(self):
#         """Method to calculate the area of the circle."""
#         import py_math
#         return py_math.pi * (self._radius ** 2)
#
# # Using the Circle class
# circle = Circle(5)
# print(f"Radius: {circle.get_radius()}")  # Accessing the radius using the getter method
# print(f"Area: {circle.get_area()}")     # Accessing the area using the method
#
# circle.set_radius(10)                   # Using the setter to update the radius
# print(f"Updated Radius: {circle.get_radius()}")
# print(f"Updated Area: {circle.get_area()}")
#
# # Trying to set a negative radius will raise an exception
# try:
#     circle.set_radius(-5)
# except ValueError as e:
#     print(e)
#
#
#
# # With decorator @property
# class Circle2:
#     def __init__(self, radius):
#         self._radius = radius  # Use a protected variable to store the radius
#
#     @property
#     def radius(self):
#         """Getter method for the radius."""
#         return self._radius
#
#     @radius.setter
#     def radius(self, value):
#         """Setter method for the radius with validation."""
#         if value < 0:
#             raise ValueError("Radius cannot be negative")
#         self._radius = value
#
#     @property
#     def area(self):
#         """Read-only property to calculate the area of the circle."""
#         import py_math
#         return py_math.pi * (self._radius ** 2)
#
# # Using the Circle class
# circle2 = Circle2(5)
# print(f"Radius: {circle2.radius}")  # Accessing the radius using the property
# print(f"Area: {circle2.area}")      # Accessing the area using the read-only property
#
# circle2.radius = 10                 # Using the setter to update the radius
# print(f"Updated Radius: {circle2.radius}")
# print(f"Updated Area: {circle2.area}")
#
# # Trying to set a negative radius will raise an exception
# try:
#     circle2.radius = -5
# except ValueError as e:
#     print(e)
