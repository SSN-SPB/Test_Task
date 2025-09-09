#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest as ut

one_list = [-2, 31, 5, 6]
two_list = [-12, 311, 15, 61]


class ZipTest(ut.TestCase):
    def test_combing_to_tuple(self):
        result = get_tuple_from_zip(one_list, two_list)
        self.assertEqual(((-2, -12), (31, 311), (5, 15), (6, 61)), result)


def get_tuple_from_zip(list_one, list_two):
    test_tuple = tuple(zip(list_one, list_two))
    return test_tuple


def main():
    return True


if __name__ == "__main__":
    main()
    ut.main(verbosity=3)
