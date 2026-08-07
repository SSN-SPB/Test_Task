def sugar_decorator(func):
    def wrapper(n):
        if n < 0:
            return "Value is not corrrect"
        else:
            print(f"Calculate interim value of factorial for {n}")
            return func(n)

    return wrapper


@sugar_decorator
def factorial_via_recursion(n):
    if n == 0:
        return 1
    return n * factorial_via_recursion(n - 1)


def starting_code(n):
    print(f"the final value for {n} is {factorial_via_recursion(n)}")


if __name__ == "__main__":
    starting_code(5)
    starting_code(-5)
