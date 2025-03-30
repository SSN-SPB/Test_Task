# Importing wraps: The wraps decorator from the functools module is used to
# wrap the wrapper function, ensuring it carries over the metadata from func.

from functools import wraps


def decorator(func):
    # @wraps(func)
    def wrapper(a, b):
        print(f"execute function {func.__name__}, than  {func.__doc__}")
        return func(a, b)

    return wrapper


@decorator
def count_sum(a, b):
    """counts sum of two int values"""
    return a + b


def main():
    result = count_sum(3, 7)
    print(result)


if __name__ == "__main__":
    main()
