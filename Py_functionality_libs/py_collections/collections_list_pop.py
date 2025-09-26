# list pop removes element - last or by index


def main():
    list1 = [0, 1, 2, 3, 4, 5, 6]
    list1.pop()
    print(list1)  # [0, 1, 2, 3, 4, 5]
    list1.pop(3)
    print(list1)


if __name__ == "__main__":
    main()
