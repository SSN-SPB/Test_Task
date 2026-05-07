# The @classmethod decorator in Python is used to define a method
# that belongs to the class rather than an instance of the class.
# Class methods take the class itself as the first argument,
# conventionally named 'cls',
# and can access and modify class state that applies across all instances of the class.
# They are often used for factory methods that create instances of the class
# or for methods that operate on class-level data.

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population


def main():
    s = Person
    logger.info(s.get_population())
    p1 = Person("Alice")
    p2 = Person("Bob")
    p3 = Person("Tom")
    logger.info(s.get_population())


if __name__ == "__main__":
    main()
