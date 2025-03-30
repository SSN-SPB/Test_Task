from decimal import Decimal


def main():
    d = sum_of_three(0.012)
    print(d)  # 0.036000000000000004
    y = d
    print(y)
    print(type(y))
    print(Decimal(y))
    print(Decimal(y))


def sum_of_three(a):
    return a + a + a


if __name__ == "__main__":
    main()
