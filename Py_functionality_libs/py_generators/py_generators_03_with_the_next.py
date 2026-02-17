def count_plus(i):
    for x in range(0, i):
        print(f"i = {i}")
        print(f"x = {x}")
        yield x + i


def main():
    plus_three = count_plus(8)
    print(next(plus_three))
    print(next(plus_three))
    print(next(plus_three))
    print(next(plus_three))
    print(next(plus_three))
    # Iterate through the generator until it is exhausted
    for value in plus_three:
        print(f"The next is found: {value}")


if __name__ == "__main__":
    main()
