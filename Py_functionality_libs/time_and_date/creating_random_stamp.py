#!/usr/bin/env python3
import string
import random


def random_stampe(x):
    letters = string.ascii_lowercase
    random_stamp = ''.join(random.choice(letters) for i in range(x))
    return random_stamp


def main(z):
    stamp = random_stampe(z)
    return stamp


if __name__ == '__main__':
    result = main(15)

print(r'It displays random combination of leters'.center(80, '/'))
print(result)
