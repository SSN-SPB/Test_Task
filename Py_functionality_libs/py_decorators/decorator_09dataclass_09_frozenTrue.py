# dataclass(frozen=True) is a decorator that can be applied
# to a class to make object immutable after creating.
from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    name: str
    age: int


def main():
    tom = Person("Tom", 33)
    print(tom.name)
    print(tom.age)
    try:
        tom.age = 37
    except Exception as fie:
        print(fie)
    print(tom.age)


if __name__ == "__main__":
    main()
