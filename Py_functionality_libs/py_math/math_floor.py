import math


def return_round(n, r):
    return round(n, r)


def main():
    result = round(3.14159, 3)
    print(result)
    print(math.floor(result))
    print(result / 1)
    print(round(result, 0))
    assert math.floor(result) == round(result, 0)


if __name__ == "__main__":
    main()
