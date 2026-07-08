def count_plus(i):
    for x in range(0, i):
        yield x + i
        yield x + i + 1


def main():
    for y in count_plus(7):
        print(y)
    print(count_plus(17))


if __name__ == "__main__":
    main()
