# The @staticmethod decorator in Python is used to define a method
# that belongs to a class rather than an instance of the class.
# Static methods do not have access to the instance (self)
# or class (cls) variables and are typically used for
# utility functions that perform a task in isolation
# from the class or instance state.


class Counter:
    def __init__(self, argument_one, argument_two):
        self.argument_one = argument_one
        self.argument_two = argument_two

    @staticmethod
    def count_sum(a, b):
        return a + b

    def count_difference(self):
        return self.argument_one - self.argument_two


def main():
    s = Counter.count_sum(3, 7)
    print(s)
    d = Counter(7, 2)
    diff = d.count_difference()
    print(diff)


if __name__ == "__main__":
    main()
