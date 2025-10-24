def gnr():
    gen = (x * x for x in range(3))
    print(gen)
    # yield
    print(set(gen))
    return gen


def main():
    print(gnr())  # <generator object gnr.<locals>.<genexpr> at 0x000001C7EBE2A9B0>
    gen2 = (x * x for x in range(3))
    print(next(gen2))  # 0
    print(next(gen2))  # 1
    print(next(gen2))  # 4


if __name__ == "__main__":
    main()
