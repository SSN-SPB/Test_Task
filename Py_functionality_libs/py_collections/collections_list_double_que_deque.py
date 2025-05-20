# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# list 40:00
from collections import deque


def main():
    list1 = [0, 7, 2, 3, 4, 5, 6]
    dq = deque(list1)
    dq.appendleft("dq1")
    print(list1)  # [0, 7, 2, 3, 4, 5, 6]
    print(dq)  # deque(['dq1', 0, 7, 2, 3, 4, 5, 6])
    for x in dq:
        print(x)
    dq.popleft()  # deque([0, 7, 2, 3, 4, 5, 6])
    print(dq)
    dq.pop()
    print(dq)  # deque([0, 7, 2, 3, 4, 5])
    print(list1)  # [0, 7, 2, 3, 4, 5, 6]


if __name__ == "__main__":
    main()
