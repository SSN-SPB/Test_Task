def lambda_multiply(y: int):
    return lambda x: x * y


def main():
    double_value = lambda_multiply(2)
    tripple_value = lambda_multiply(3)
    print(double_value(5) == 10)
    print(tripple_value(7) == 21)
    assert double_value(5) == 10


if __name__ == "__main__":
    main()
