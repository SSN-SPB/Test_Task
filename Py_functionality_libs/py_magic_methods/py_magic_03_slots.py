# __slots__ is a special attribute in Python classes
# that allows you to explicitly declare
# data members (attributes) and prevent
# the creation of __dict__ for each instance.
# This can lead to memory savings and faster
# attribute access, but it also means that you cannot
# add attributes dynamically to instances of the class.


class OptimizedClass:
    __slots__ = ["name", "age"]  # Indicating fixed attributes

    def __init__(self, name, age):
        self.name = name
        self.age = age


class OptimizedClass2:
    # __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():
    obj = OptimizedClass("Ivan", 32)
    print(obj.name)  # Ivan
    print(obj.age)  # 32

    try:
        obj.address = "Moscow"  # Error: Not allowded to add new attribute
    except AttributeError as e:
        print(e)  # "'OptimizedClass' object has no attribute 'address'"
    try:
        print(obj.__dict__)  # AttributeError: 'OptimizedClass' object
        # has no attribute '__dict__'
    except AttributeError as e:
        print(e)

    obj2 = OptimizedClass2("Ivan", 32)
    print(obj2.name)  # Ivan
    print(obj2.age)  # 32

    obj2.address = "Moscow"  # Adding new attribute is allowed
    print(obj2.address)  # Moscow
    print(obj2.__dict__)  # {'name': 'Ivan', 'age': 32, 'address': 'Moscow'}


if __name__ == "__main__":
    main()
