"""Suite demonstrates polymorphism overriding in oop Python"""

# Runtime Polymorthism


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


def main():
    fg_test = Figure()
    sq_test = Square()
    fg_test.setup()
    sq_test.setup()
    print(f" The area of {fg_test.__class__.__name__} is {fg_test.count_area()}")
    print(f" The area of {sq_test.__class__.__name__} is {sq_test.count_area()}")
    print(f" The area of {sq_test.__class__.__name__} is {sq_test.count_area(5, 6)}")


if __name__ == "__main__":
    main()
