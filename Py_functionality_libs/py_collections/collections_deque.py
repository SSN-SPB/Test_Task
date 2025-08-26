from collections import deque


def main():
    list_test = (1, 2, 3)
    d = deque(list_test)
    d.append(4)
    d.appendleft(-1)
    d.appendleft("x")
    print(list_test)   # (1, 2, 3)
    print(d)           # deque(['x', -1, 1, 2, 3, 4])
    print(type(d))     # <class 'collections.deque'>
    print(list_test)
    list_test = list(d)
    print(list_test)   # ['x', -1, 1, 2, 3, 4]


if __name__ == "__main__":
    main()
