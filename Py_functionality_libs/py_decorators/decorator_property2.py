# The @property decorator in Python is used to define
# a method that can be accessed like an attribute.
# It's often used to encapsulate data, providing a
# way to define getter, setter, and delete methods
# while maintaining a clean interface.
# with decorator @property


class Square:

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    @property
    def count_square(self):
        return self.side_a * self.side_b


def main():
    s = Square(7, 8)
    print(s.count_square)


if __name__ == main():
    main()
