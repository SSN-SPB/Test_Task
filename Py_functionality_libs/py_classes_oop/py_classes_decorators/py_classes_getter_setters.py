class Circle:
    def __init__(self, radius):
        self._radius = radius  # private attribute

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * (self._radius**2)


def main():
    circle = Circle(5)
    print(circle.radius)  # 5 (getter in action)
    circle.radius = 10  # Setter validates the value
    print(circle.area)  # 314.159 (read-only property)

    # circle.area = 100  # ❌ This will raise an AttributeError
    # circle.radius = -3 # ❌ Raises ValueError: Radius cannot be negative


if __name__ == "__main__":
    main()
