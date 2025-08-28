#!/usr/bin/env python3


class Counter:
    count = 5

    def __init__(self, name):
        self.count = 7
        self.name = name


def main():
    s = Counter("Sergei")
    print(vars(s))
    print(vars(Counter))
    print(vars(Counter("Ivan")))



if __name__ == "__main__":
    main()
