# decorators are used to modify the behavior of functions or classes.
# They are a powerful tool in Python that allows you to add
# functionality to existing code without modifying it directly.
# In this example, we will explore the use of class methods
# and how they can be used to manipulate class-level data.
# @classmethod is a built-in decorator in Python that is used
# to define a method as a class method. A class method is a
# method that belongs to the class rather than an instance of
# the class. It takes the class itself as the first argument,
# conventionally named 'cls'. Class methods can access and
# modify class state that applies across all instances of the class.
# They are often used for factory methods that create instances of
# the class or for methods that operate on class-level data.


class Counter:
    count = 5

    def __init__(self):
        self.count = 7

    @classmethod
    def count_increase(cls, number):
        result = cls.count + number
        return result

    def get_count(self):
        # print(self.value)
        return self.count

    def increased_instance(self, nums):
        return self.count + nums

    def enlarge_instance(self, nums):
        self.count = self.count + nums


def main():
    s = Counter()
    print(vars(s))  # {'count': 7}
    s.count_increase(3)
    s1 = Counter.count_increase(7)
    print(s1)  # 12
    print(vars(s))  # {'count': 7}
    print(s.increased_instance(3))  # 10
    print(vars(s))  # {'count': 7}
    print(s.get_count())  # 7
    s.enlarge_instance(10)
    print(vars(s))  # {'count': 17}
    assert vars(s) == {"count": 17}


if __name__ == "__main__":
    main()
