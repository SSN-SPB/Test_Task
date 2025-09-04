# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# list 20- 25
# concatenate += 26


def main():
    list1 = [x**2 for x in [1, 2, 3]]
    assert list1 == [1, 4, 9]
    list2 = [x * 3 for x in ["a", "b"]]
    assert list2 == ["aaa", "bbb"]
    list3 = [x * 3 for x in ("a", "b")]
    assert list3 == list2
    list5 = [x**2 for x in range(1, 4)]
    assert list5 == [1, 4, 9]


if __name__ == "__main__":
    main()
