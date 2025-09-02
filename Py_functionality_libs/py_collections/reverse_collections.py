# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# reversed 5:15


def main():
    xs = ("Ivan", "Petrov", "June25", 12, 1947)
    print("reversed cortege is object{}".format(reversed(xs)))
    print("reversed cortege moved to list {}".format(list(reversed(xs))))
    print("cortege to reversed cortege {}".format(tuple(reversed(xs))))
    print("slice does the same but consumes more memory ".center(79, "/"))
    print("cortege to reversed cortege {}".format(xs[::-1]))
    print("cortege to reversed cortege {}".format(xs[::-2]))


if __name__ == "__main__":
    main()
