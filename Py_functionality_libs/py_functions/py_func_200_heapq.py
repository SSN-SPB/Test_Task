#!/usr/bin/env python3
import heapq
import random


def generate_random_list():
    x = [random.randint(0, 21) for _ in range(100)]
    print(x)
    return x


def main():
    y = generate_random_list()
    print(heapq.nsmallest(19, y))
    print(heapq.nlargest(19, y))


if __name__ == "__main__":
    main()
