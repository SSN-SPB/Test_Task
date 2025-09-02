import itertools


def main():
    list0 = [0, 1]
    list1 = ["a", "b"]
    list2 = ["с", "в"]
    list_result = list(itertools.chain(list2, list1, list0))
    assert list_result == ["с", "в", "a", "b", 0, 1]

    set0 = (0, 1)
    list1 = ["a", "b"]
    list2 = ["с", "в"]
    list_result2 = list(itertools.chain(list2, list1, set0, list1))
    assert list_result2 == ["с", "в", "a", "b", 0, 1, "a", "b"]


if __name__ == "__main__":
    main()
