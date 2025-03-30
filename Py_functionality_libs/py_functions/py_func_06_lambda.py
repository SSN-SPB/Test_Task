def main():
    print(list(map(lambda a: a + a + a, range(0, 10, 2))))
    print(list(map(lambda x: x + 100, range(10))))


if __name__ == "__main__":
    main()
