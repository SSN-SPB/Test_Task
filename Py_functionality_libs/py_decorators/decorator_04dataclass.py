# The @classmethod decorator in Python is used to define a method
# that belongs to the class rather than an instance of the class.
# Class methods take the class itself as the first argument,
# conventionally named 'cls',
# and can access and modify class state that applies across all instances of the class.
# They are often used for factory methods that create instances of the class
# or for methods that operate on class-level data.

import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def make_some_calculation(self, x, y) -> int:
        return x**2 + y**2


def main():
    p = Point(3, 4)
    logger.info(p)
    logger.info(p.make_some_calculation(p.x, p.y))


if __name__ == "__main__":
    main()
