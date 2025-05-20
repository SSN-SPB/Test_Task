# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# Cortege one element


def main():
    xs = (42,)  # It is cortege - better this way
    print("type of (42,) is {}".format(type(xs)))
    xy = 42  # It is int
    print("type of (42) is {}".format(type(xy)))
    xz = (42,)  # It is cortege too but better (42,)
    print("type of 42, is {}".format(type(xz)))
    xzz = 42  # It is int
    print("type of 42 is {}".format(type(xzz)))
    print(" uppacking ".center(79, "/"))
    y = xs
    print("type is {}; value is {}".format(type(y), y))
    [w] = xs  # it is better
    print("it is better - type is {}; value is {}".format(type(w), w))


if __name__ == "__main__":
    main()
