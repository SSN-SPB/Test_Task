def classic_generator():
    for i in range(5):
        print(f"current value is {i}")
        yield i


def main():
    x = classic_generator()
    try:
        print(next(x))
        print(next(x))
        print(next(x))
        print(next(x))
        print(next(x))
        print(next(x))
        print(next(x))
        print(next(x))
        print(next(x))
    except StopIteration as ci:
        print(ci.__doc__)


if __name__ == "__main__":
    main()
