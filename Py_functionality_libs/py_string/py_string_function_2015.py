#!/usr/bin/env python3
# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/
import os


# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/

def main():
    print('Combining strings'.center(80, '/'))
    s = 'str1_' 'str2_' 'str3_' 'str4_'
    print(s)  # str1_str2_str3_str4_

    print('Checking the case treating "foo bar"'.center(80, '/'))
    strng = 'foo bar'
    print('capitalize(): {}'.format(strng.capitalize()))  # Foo bar
    print('title(): {}'.format(strng.title()))  # Foo Bar
    print('upper(): {}'.format(strng.upper()))  # Foo Bar
    print('Checking the case treating "foo BAr"'.center(80, '/'))
    strng = 'foo BAr'  # FOO BAR
    print('lower(): {}'.format(strng.lower()))  # foo bar
    print('swap(): {}'.format(strng.swapcase()))  # FOO baR
    # justification
    print('Checking the case treating "Foo bar."'.center(80, '/'))
    strng = 'Foo bar.'
    print('ljust(): {}'.format(strng.ljust(15, '/')))  # Foo bar.///////
    print('rjust(): {}'.format(strng.rjust(15, '/')))  # ///////Foo bar.
    print('center(): {}'.format(strng.center(15, '/')))  # ////Foo bar.///
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


if __name__ == '__main__':
    main()
