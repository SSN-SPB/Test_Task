#!/usr/bin/env python3
# Copyright 2021 Sergei Smirnov


words_list = ['aaa', 'bbb', 'SpartakMoscow', 'ccc']


class OwnException(Exception):
    """Some word that is considered as unpropriate is found"""
    print('Not valid word is used')


def check_the_words(list_of_words, not_allowed_word):
    for x in list_of_words:
        if x == str(not_allowed_word):
            raise OwnException


def main():
    try:
        check_the_words(words_list, 'SpartakMoscow')
    except OwnException as e:
        print(e.__doc__)


if __name__ == '__main__':
    main()
