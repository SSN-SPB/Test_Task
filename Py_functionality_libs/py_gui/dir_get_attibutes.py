# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# set 52:00
# dictionary
# get - returns new value if key is not in dictionary


def main():
    d = dict(xkey="xvalue", ykey="yvalue")
    print("dict d: {}".format(d))
    # dict d: {'xkey': 'xvalue', 'ykey': 'yvalue'}
    print("dict d: key {} has value '{}'".format("xkey", d["xkey"]))
    # dict d: key xkey has value 'xvalue'
    try:
        print("dict d: notexistinkey {} has value '{}'".format("zkey", d["zkey"]))
    except KeyError as e:
        print(e)
        print(dir(e))
        print(e.__getattribute__)
        print(e.with_traceback)


if __name__ == "__main__":
    main()
