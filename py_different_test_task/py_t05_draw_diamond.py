def draw_diamond(size: int):
    test_list = []
    for i in range(0, size):
        print(" " * (size - i) + "*" * i * 2 + "*")
        test_list.append(" " * (size - i) + "*" * i * 2 + "*")
    for x in test_list[::-1]:
        if test_list[::-1].index(x) > 0:
            print(x)


def main():
    for x in range(2, 8, 2):
        draw_diamond(x)


if __name__ == "__main__":
    main()
