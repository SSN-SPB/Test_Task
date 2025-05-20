# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# reversed 5:15


def main():
    xs = ("Ivan", "Petrov", "June", 12, 1947)
    print("reversed cortege is object{}".format(reversed(xs)))
    print("reversed cortege moved to list {}".format(list(reversed(xs))))
    print("cortege to reversed cortege {}".format(tuple(reversed(xs))))
    print("slice does the same but consumes more memory ".center(79, "/"))
    print("cortege to reversed cortege {}".format(xs[::-1]))
    print("cortege to reversed cortege {}".format(xs[::-2]))


# reversed cortege is object<reversed object at 0x060FA670>
# reversed cortege moved to list [1947, 12, 'June', 'Petrov', 'Ivan']
# cortege to reversed cortege (1947, 12, 'June', 'Petrov', 'Ivan')
# /////////////////slice does the same but consumes more memory /////////////////
# cortege to reversed cortege (1947, 12, 'June', 'Petrov', 'Ivan')
# cortege to reversed cortege (1947, 'June', 'Ivan')


if __name__ == "__main__":
    main()
