list1 = [0, 1, 2, 3, 4, 5, 6]


def main():
    reversed_list = list1[::-1]
    reversed_list2 = reversed(list1)
    # reversed_list2 is an iterator, so we need to
    # convert it to a list to compare
    # but in moment of creating reversed_list2 saves
    # memory, because it doesn't
    # create a new list, but just iterates over the
    # original list in reverse order
    for _ in reversed_list2:
        print(_)
    reversed_list2 = list(reversed_list2)
    print("reversed list with slice {}".format(reversed_list))
    print("reversed list with reversed() {}".format(reversed_list2))
    assert reversed_list == reversed_list2


if __name__ == "__main__":
    main()
