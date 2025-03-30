"""Suite demonstrates inheritance in oop Python"""

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


class BuyTest(BaseClass, SecondBaseClass):

    def run(self):
        print(self)
        print("make run buy")

    def setup(self):
        print(self)
        print("make setup BuyTestClass")


def main():
    print(BuyTest.mro())
    buy_test = BuyTest()
    buy_test.setup()


if __name__ == "__main__":
    main()

# lt_test2 = LoginTest()
# lt_test2.setup()
