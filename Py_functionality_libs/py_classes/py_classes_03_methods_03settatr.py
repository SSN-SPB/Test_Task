# settatr() is a built-in function that allows you
# to set an attribute of an object (but not to class) to a specific value.
# It takes three arguments: the object,
# the name of the attribute as a string, and the value to set.


class Counter:
    def __init__(self):
        self.count = 7
        self.name = "value"

    def count_increase(self, number):
        self.count = self.count + number
        return self.count

    def get_count(self):
        return self.count


def main():
    s = Counter()
    print(vars(s))  # {'count': 7, 'name': 'value'}
    s.count_increase(3)
    print(vars(s))  #
    print(s.get_count())  # 10 (7 + 3)
    s2 = Counter()
    setattr(s, "location", "shelf B:1")
    print(vars(s))  # {'count': 10, 'name': 'value', 'location': 'shelf B:1'}
    print(vars(s2))  # {'count': 7, 'name': 'value'}
    assert vars(s) == {"count": 10, "name": "value", "location": "shelf B:1"}
    assert vars(s2) == {"count": 7, "name": "value"}


if __name__ == "__main__":
    main()
