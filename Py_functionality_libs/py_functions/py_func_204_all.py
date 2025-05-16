"""
The all() function returns True if all items in
an iterable are true, otherwise it returns False.
"""

mylist = [0, 1, 1]
mylist2 = [3 > 1, 1, 1]
mytuple = (0, True, False)
myset = {0, 1, 0}
mydict = {7: "0", 1: "Orange"}


def check_all(iterable_object):
    return all(iterable_object)


def main():
    assert check_all(mylist) is False
    assert check_all(mylist2) is True
    assert check_all(mytuple) is False
    assert check_all(myset) is False
    assert check_all(mydict) is True


if __name__ == "__main__":
    main()
