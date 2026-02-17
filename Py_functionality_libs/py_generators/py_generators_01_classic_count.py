def count_plus(i):
    for x in range(0, i):
        yield x + i


def main():
    for y in count_plus(5):
        print(y)


if __name__ == "__main__":
    main()
