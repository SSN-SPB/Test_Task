#!/usr/bin/env python3


class Counter:
    count = 5

    def __init__(self):
        self.count = 7

    @classmethod
    def count_increase(cls, number):
        result = cls.count + number
        return result

    def get_count(self):
        return self.count


def main():
    s = Counter()
    print(s)  # <__main__.Counter object at 0x00000275A627A390>
    s1 = s.count_increase(19)
    print(s1)  # 24
    print(Counter.count_increase(119))  # 124
    z = s.get_count()  # 24
    print(int(z))  # 7


if __name__ == "__main__":
    main()
