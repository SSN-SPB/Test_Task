def main():
    print(list(map(lambda a: a + a + a, range(0, 10, 2))))
    print(list(map(lambda x: x + 100, range(10))))
    print(
        list(
            map(
                lambda x, y: x + y,
                range(10),
                [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],
            )
        )
    )


if __name__ == "__main__":
    main()
