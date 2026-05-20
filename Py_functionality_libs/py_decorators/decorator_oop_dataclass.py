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
