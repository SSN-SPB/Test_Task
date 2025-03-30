#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

list_a = ["a", "a1", "a2"]
list_b = ["b", "b1", "b2"]
expected_list = ['a', 'a1', 'a2', 'b', 'b1', 'b2']


class MyTestCase(unittest.TestCase):
    def test_extended_list(self):
        tested_list = extend_list(list_a, list_b)
        self.assertEqual(tested_list, expected_list)


def extend_list(list_one, list_two):
    list_one.extend(list_two)
    return list_one


def main():
    list_b.extend(list_a)
    print(list_b)
    list_a.append(list_b)
    print(list_a)


if __name__ == "__main__":
    main()
    unittest.main(verbosity=3)
