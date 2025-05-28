"""Uses shared objects to minimize memory usage."""

# https://python-patterns.guide/gang-of-four/flyweight/


class Flyweight:
    _instances = {}

    def __new__(cls, shared_state):
        if shared_state not in cls._instances:
            cls._instances[shared_state] = super(Flyweight, cls).__new__(cls)
            cls._instances[shared_state].state = shared_state
        return cls._instances[shared_state]


def main():
    obj1 = Flyweight("shared")
    obj2 = Flyweight("shared")
    print(obj1 is obj2)  # Output: True (same instance)


if __name__ == "__main__":
    main()
