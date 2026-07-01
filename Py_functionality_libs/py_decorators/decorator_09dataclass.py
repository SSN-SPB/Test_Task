from dataclasses import dataclass
import logging

# The @dataclass decorator in Python is used to
# automatically generate special methods for classes,
# such as __init__, __repr__, __eq__,
# and others, based on the class attributes.
# This simplifies the process of creating classes
# that are primarily used to store data,
# as it reduces boilerplate code and enhances readability.


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass(order=True)  # order=True добавляет методы сравнения
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
