# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# set 48:00
# dictionary
# dict - short constructor


def main():
    d = dict(xkey="xvalue", ykey="yvalue")
    print("dict d: {}".format(d))
    # dict d: {'xkey': 'xvalue', 'ykey': 'yvalue'}
    # adding new value via constructor
    d = dict(d, zkey="zvalue")
    print("dict d: {}".format(d))
    # dict d: {'xkey': 'xvalue', 'ykey': 'yvalue', 'zkey': 'zvalue'}
    # dictionary methods
    print("keys of d: {}".format(d.keys()))
    # keys of d: dict_keys(['xkey', 'ykey', 'zkey'])
    for x in d.keys():
        print(x)
    print("values of d: {}".format(d.values()))
    # values of d: dict_values(['xvalue', 'yvalue', 'zvalue'])
    print("items of d: {}".format(d.items()))
    # items of d:\
    # dict_items([('xkey', 'xvalue'), ('ykey', 'yvalue'), ('zkey', 'zvalue')])
    print("len of d: {}".format(len(d.items())))  # len of d: 3


if __name__ == "__main__":
    main()
