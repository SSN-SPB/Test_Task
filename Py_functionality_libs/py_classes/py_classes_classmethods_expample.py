#!/usr/bin/env python3


class Counter:
    count = 5

    def __init__(self):
        self.count = 7

    @classmethod
    def count_increase(cls, number):
        result = cls.count + number
        # print(result)
        return result

    def get_count(self):
        # print(self.value)
        return self.count


def main():
    s = Counter()
    print(s.count_increase(19))
    print(Counter.count_increase(119))
    z = s.get_count()
    print(int(z))


if __name__ == "__main__":
    main()
