# this is a simple fibonacci function with recursion and
# decorator to check the input argument


def checker_fibonacci(func):
    def wrapper(n):
        if not isinstance(n, int):
            return "The argument should be integer"
        if n < 0:
            return "The argument should be positive and > 1"
        else:
            return func(n)

    return wrapper


@checker_fibonacci
def fibonacci(y):
    if y <= 1:
        return y
    else:
        interim = fibonacci(y - 1) + fibonacci(y - 2)
        return interim


def main(y):
    fibonacci_list = list()
    print(f"Start fibonacci list calculating for {y} elements")
    for x in range(y):
        fibonacci_list.append(fibonacci(x))

    print(fibonacci_list)
    print(fibonacci(-y))
    print(fibonacci(5.0))


if __name__ == "__main__":
    main(10)
