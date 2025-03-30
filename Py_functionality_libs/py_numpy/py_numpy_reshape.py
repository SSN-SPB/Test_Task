#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import unittest


class MyTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_second_element(self):
        x = int(get_second_element())
        self.assertEqual(7, x)


def get_second_element():
    b = np.array(["x", 7, True, "y", 2, False])
    print(b[1])
    return b[1]



def main():
    a = np.array(["x", 1, True, "y", 2, False])
    print(a)
    a = a.reshape(2, 3)
    print(a)
    get_second_element()
    return a


if __name__ == "__main__":
    main()
    unittest.main(verbosity=2)
