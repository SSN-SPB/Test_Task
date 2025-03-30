#!/usr/bin/env python3

import os


# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/

def main():
    print('Checking the case treating'.center(80, '/'))
    strng = 'foo bar'
    print(strng.capitalize())  # Foo bar
    print(strng.title())  # Foo Bar
    print(strng.upper())  # Foo Bar
    strng = 'foo BAr'  # FOO BAR
    print(strng.lower())  # foo bar
    print(strng.swapcase())  # FOO baR
    # justification
    print('Checking the justification symbol'.center(80, '/'))
    strng = 'Foo bar.'
    print(strng.ljust(15, '/'))  # Foo bar.///////
    print(strng.rjust(15, '/'))  # ///////Foo bar.
    print(strng.center(15, '/'))  # ////Foo bar.///
    # remove symbols left and right
    print('Checking the removing the symbol'.center(80, '/'))
    strng = ']>>>Foo bar.<<<['
    print(strng.lstrip(']'))  # >>>Foo bar.<<<[
    print(strng.lstrip('>'))  # ]>>>Foo bar.<<<[
    print(strng.lstrip(']>'))  # Foo bar.<<<[
    print(strng.rstrip(']'))  # ]>>>Foo bar.<<<[
    print(strng.rstrip('<['))  # ]>>>Foo bar.
    print(strng.strip('[]><'))  # Foo bar.
    print(strng.strip('><[]'))  # Foo bar.
    print(strng.strip('><[].'))  # Foo bar
    print(strng.strip('><[r].'))  # Foo ba
    print(strng.strip('>r<[].'))  # Foo ba
    # ignore specail symbols
    print('ignore specail symbols'.center(80, '/'))
    strng = '\tell me'  # ell me
    print(strng)  # ell me
    print(r' \tell me')  # \tell me
    # multiline demo
    print(''' foo
    bar

    string''')
    # foo
    #    bar
    #
    #    string
    print('foo-'
          'bar-'
          'line!')  # foo-bar-line!


if __name__ == '__main__': result = main()
