"""Suite demonstrates call magic methods in oop Python"""

# The __call__ method in Python is a special method
# that allows an instance of a class to be called as if it were a function.
#
# When you define the __call__ method in a class, you
# can create an instance of that class and then call
# it like a regular function, passing arguments to it.
#
# The __call__ method can be used to make an object
# behave like a function, which can be useful for
# various purposes, such as creating callable objects,
# implementing function-like behavior in classes, or even creating decorators.


class UpdateDeata:
    def __call__(self, value):
        return self.factor * value

    def __init__(self, factor):
        self.factor = factor


def main():
    test_run = UpdateDeata(7)
    for i in range(1, 11):
        print(test_run(i))


if __name__ == "__main__":
    main()
