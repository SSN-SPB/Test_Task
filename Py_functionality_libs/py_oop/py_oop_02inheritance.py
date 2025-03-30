"""Suite demonstrates inheritance in oop Python"""

class BaseClass:
    """__ph__"""

    def setup(self):
        print(self)
        print("make setup base")



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


class BuyTest(BaseClass):

    def run(self):
        print(self)

        print("make run buy")


def main():
    print("main")
    bt_test = BuyTest()
    lt_test = LoginTest()
    lt_test.setup()
    bt_test.setup()


if __name__ == "__main__":
    main()

# lt_test2 = LoginTest()
# lt_test2.setup()
