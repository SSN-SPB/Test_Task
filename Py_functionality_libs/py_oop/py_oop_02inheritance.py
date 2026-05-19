"""Suite demonstrates inheritance in oop Python"""

# Inheritance is a fundamental concept in object-oriented programming (OOP)
# that allows a new class (called a child or subclass) to inherit attributes and methods
# from an existing class (called a parent or superclass).
# This promotes code reusability and establishes a natural hierarchical relationship between classes.
# In Python, inheritance is implemented by defining
# a new class that specifies the parent class in parentheses after the class name.


class BaseClass:
    """__ph__"""

    def setup(self):
        print(f"from BaseClass setup {self}")
        print("make setup base")


class LoginTest(BaseClass):
    """__ph__"""

    def __init__(self):
        print(f"activate {self.__class__.__name__}")

    def run(self):
        print(self)
        print("make run login")

    def setup(self):
        print(f"from LoginTest setup {dir(self)}")
        print("make setup login and override the base class")


class BuyTest(BaseClass):

    def __init__(self):
        print(f"activate {self.__class__.__name__}")

    def run(self):
        print("make run buy")


def main():
    print("main")
    bt_test = BuyTest()
    lt_test = LoginTest()
    lt_test.setup()
    bt_test.setup()


if __name__ == "__main__":
    main()
