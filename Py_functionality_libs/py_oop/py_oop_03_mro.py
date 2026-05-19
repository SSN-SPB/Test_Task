"""Suite demonstrates mro in oop Python"""

# MRO (Method Resolution Order) is a mechanism in Python
# that determines the order in which base classes
# are searched when looking for a method or attribute in a class hierarchy.
# It is particularly important in the context of multiple inheritance, where a class can inherit


class BaseClass:
    """__ph__"""

    def setup(self):
        print(self)
        print("make setup base")


class SecondBaseClass:
    """__ph__"""

    def setup(self):
        print(self)
        print("make second setup base")


class LoginTest(BaseClass):
    """__ph__"""

    def run(self):
        print(self)
        print("make run login")

    def setup(self):
        print(self.__class__)
        print(self.__dir__)
        print(dir(self))
        print("make setup login and override the base class")


# class BuyTest(SecondBaseClass, BaseClass):
class BuyTest(BaseClass, SecondBaseClass):

    def run(self):
        print(self)
        print("make run buy")

    def setup(self):
        print(self)
        print("make setup BuyTestClass")


def main():
    print(f"MRO: of class BuyTest(BaseClass, SecondBaseClass) {BuyTest.mro()}")
    buy_test = BuyTest()
    buy_test.setup()
    buy_test.run()


if __name__ == "__main__":
    main()

# lt_test2 = LoginTest()
# lt_test2.setup()
