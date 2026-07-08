# classmethods are methods that are bound to
# the class and not the instance of the class.
# They can be called on the class itself or on
# an instance of the class. They take a reference
# to the class as their first parameter, which is usually named cls.
# vars() is a built-in function in Python that returns the __dict__
# attribute of an object, which is a dictionary containing the
# object's writable attributes. When called without arguments,
# vars() acts like locals() and
# returns a dictionary of the current local symbol table.



class Counter:
    count = 5

    def __init__(self):
        self.count = 7
        self.name = "value"

    @classmethod
    def count_increase(cls, number):
        result = cls.count + number
        return result

    def get_count(self):
        return self.count


def main():
    s = Counter()
    print(vars(s))  # {'count': 7, 'name': 'value'}
    s.count_increase(3)
    print(vars(s))  # {'count': 7, 'name': 'value'}
    Counter.count_increase(3)
    print(Counter.count_increase(3))  # 8 (5 + 3)
    s1 = Counter.count_increase(7)
    print(s1) # 12 (5 + 7)
    assert vars(s) == {"count": 7, "name": "value"}


if __name__ == "__main__":
    main()
