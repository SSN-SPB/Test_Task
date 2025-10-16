# Access by name
# Field names

from collections import namedtuple


def named_tuple_example():
    Point = namedtuple("Point", ["x", "y"])
    point = Point(10, 20)
    print(point.x)
    print(point.y)
    assert point.x == 10
    assert point.y == 20


def main2():
    named_tuple_example()


if __name__ == "__main__":
    main2()
