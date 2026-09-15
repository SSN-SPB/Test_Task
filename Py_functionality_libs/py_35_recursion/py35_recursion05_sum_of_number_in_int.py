def description(func):
    def wrapper(n):
        if not isinstance(n, int):
            print(f"Argument should be integer while {n} is {type(n)}")
            return None
        return func(n)

    return wrapper


@description
def sum_of_numbers_in_int(n: int) -> int:
    if n // 10 == 0:
        return n
    else:
        return n % 10 + sum_of_numbers_in_int(n // 10)


def check_argument(n):
    if sum_of_numbers_in_int(n):
        print(f"The sum of {n} is {sum_of_numbers_in_int(n)}")


def main():
    check_argument(552)
    check_argument("hi")


if __name__ == "__main__":
    main()
