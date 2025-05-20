# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# set 54:00
# dictionary
# setdefault - add value if key is not found or returns existing value


def main():
    d = dict(xkey="xval", ykey="yval")
    print("d: {}".format(d))  # d: {'xkey': 'xval', 'ykey': 'yval'}
    print(d.setdefault("zkey", "zval"))  # zval
    print(d.setdefault("xkey", "xxx"))  # xval


if __name__ == "__main__":
    main()
