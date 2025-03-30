# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# set 54:00
# dictionary
# OrderedDict - create dictionary with key arranged by 1st adding time
from collections import OrderedDict


def main():
    d = OrderedDict(xk='xv', ykey='yv')
    print('{}'.format(d))        # OrderedDict([('xk', 'xv'), ('ykey', 'yv')])
    print('{}'.format(list(d)))  # ['xk', 'ykey']
    print(d.setdefault('zkey', 'zv'))  # zv
    print('{}'.format(list(d)))  # ['xk', 'ykey', 'zkey']


if __name__ == "__main__":
    main()
