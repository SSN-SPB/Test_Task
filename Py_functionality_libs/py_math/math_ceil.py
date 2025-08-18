import math


def return_round(n, r):
    return round(n, r)


def main():
    result = round(3.14159, 3)
    print(result)
    print(math.ceil(result))
    print(result / 1)
    print(round(result, 0))
    assert math.ceil(result) == round(result, 0) + 1


if __name__ == "__main__":
    main()
