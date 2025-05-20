# https://compscicenter.ru/courses/python/2015-autumn/classes/1476/
# list 20- 25
# append - one element to the end
# extend - several elements to the end of list
# insert - add element by index


def main():
    list = [0, 1]
    list.append("x")
    print(list)  # [0, 1, 'x']
    try:
        list.append("y", "y")
    except TypeError:
        print("only one element can be appended to list")
    print(list)  # [0, 1, 'x']
    try:
        list.append("y", "y")
        list.extend({"y3", "y4"})
    except TypeError:
        print("only one element can be appended to list")
    print(list)  # [0, 1, 'x']
    list.extend({"y1", "y2"})
    print(list)  # [0, 1, 'x', 'y2', 'y1']
    list.insert(-1, "w2")
    print(list)  # [0, 1, 'x', 'y2', 'w2', 'y1']
    # slice
    list[:2] = "n" * 5
    print(list)  # ['n', 'n', 'n', 'n', 'n', 'x', 'y1', 'w2', 'y2']


if __name__ == "__main__":
    main()
