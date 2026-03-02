"""Suite demonstrates polymorphism overriding in oop Python"""

# Runtime Polymorthism
# Polymorphism overriding is a feature in object-oriented programming
# where a subclass provides a specific implementation of a method that is already defined in its superclass.
# The method in the subclass overrides the method in the superclass,
# allowing for dynamic method resolution at runtime. This means that when a method is called on an object,
# the version of the method that is executed is determined by the actual type of the object,
# rather than the type of the reference variable.


class Figure:
    def __init__(self):
        self.area = 7
        self.perimeter = 0

    def setup(self):
        print("start creating Figure")

    def count_area(self):
        return self.area

    def count_perimeter(self):
        return self.area


class Square(Figure):
    def __init__(self):
        self.area = 0
        self.perimeter = 0

    def setup(self):
        print("start creating Square")

    def count_area(self, side_one=1, side_two=2):
        self.area = side_one * side_two
        return self.area


class Triangle(Figure):
    def __init__(self):
        self.area = 0
        self.perimeter = 0

    def setup(self):
        print("start creating Square")

    def count_area(self, base=5, high=3):
        self.area = base * high / 2
        return self.area


def main():
    fg_test = Figure()
    sq_test = Square()
    tr_test = Triangle()
    fg_test.setup()
    sq_test.setup()
    print(f" The area of {fg_test.__class__.__name__} is {fg_test.count_area()}")
    print(f" The area of {sq_test.__class__.__name__} is {sq_test.count_area()}")
    print(f" The area of {tr_test.__class__.__name__} is {tr_test.count_area()}")
    print(f" The area of {sq_test.__class__.__name__} is {sq_test.count_area(5, 6)}")


if __name__ == "__main__":
    main()
