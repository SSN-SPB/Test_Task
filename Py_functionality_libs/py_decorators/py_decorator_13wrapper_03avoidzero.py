# This is a good example of decorator:
# decorator wraps a function and modifies its behavior.
# In this case, the decorator checks if the second argument
# is zero before performing division, preventing a division by zero error.


def avoid_zero(func):
    def wrapper(a, b):
        if b == 0:
            return 0
        else:
            return func(a, b)

    return wrapper


@avoid_zero
def foo(a: int | float, b: int | float) -> float:
    return a / b


def main():
    print(foo(123, 0))
    print(foo(123, 23))
    assert foo(123, 0) == 0
    assert int(foo(123, 23)) == 5


if __name__ == "__main__":
    main()
