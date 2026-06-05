#!/usr/bin/env python3


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
    print(vars(s))  # {'count': 7, 'name': 'value'}
    s1 = Counter.count_increase(7)
    print(s1)
    assert vars(s) == {"count": 7, "name": "value"}


if __name__ == "__main__":
    main()
