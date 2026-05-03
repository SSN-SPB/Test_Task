# The @property decorator in Python is used to define
# a method that can be accessed like an attribute.
# It's often used to encapsulate data, providing a
# way to define getter, setter, and delete methods
# while maintaining a clean interface.
# with decorator @property

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be non-negative")
        self._radius = value


def main():
    # s = Circle(-2)
    # print(s.radius)
    s = Circle(7)
    print(s.radius)


if __name__ == "__main__":
    main()
