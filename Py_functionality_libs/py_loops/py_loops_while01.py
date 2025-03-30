def example_while(x: int) -> None:
    count = 0
    while count < x:
        count = count + 1
        print("Hello while")


def example_for(x: int) -> None:
    for i in range(0, x):
        print("Hello for")


def main():
    example_while(7)
    example_for(7)


if __name__ == "__main__":
    main()
