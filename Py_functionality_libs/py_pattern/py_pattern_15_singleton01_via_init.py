#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Singleton:
    _instance = None  # Class attribute to store the single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


def main():
    s1 = Singleton()
    s2 = Singleton()
    s3 = Singleton
    s4 = s3()

    print(s1 is s2)
    print(s1 is s3)
    print(s1 is s4)
    print(s1)
    print(s3)


if __name__ == "__main__":
    main()
