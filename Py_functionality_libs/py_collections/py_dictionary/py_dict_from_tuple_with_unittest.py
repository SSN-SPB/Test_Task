#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest as ut

roll_string = ("ab", "bc")


class DictTest(ut.TestCase):
    def test_dictionary_from_tuple(self):
        result_dict = make_dictionary_from_tuple(roll_string)
        self.assertEqual({'a': 'b', 'b': 'c'}, result_dict)


def make_dictionary_from_tuple(test_tuple):
    result_dictionary = dict(test_tuple)
    return result_dictionary


def main():
    result_dict = make_dictionary_from_tuple(roll_string)
    print(result_dict)
    return True


if __name__ == "__main__":
    main()
    # ut.main(verbosity=2)
