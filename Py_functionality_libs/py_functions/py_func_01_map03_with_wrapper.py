# this python script demonstrates the use of map function with a lambda function
# and a wrapper function to ensure only positive values are processed.


def make_positive_only(func):

    def wrapper(n):
        if n < 0:
            print("The only positive values are allowed")
            n = -n
        return func(n)

    return wrapper


@make_positive_only
def increase_seven(x):
    return x + 7


def main():
    print(list(map(lambda x: x + 100, range(10))))
    print(increase_seven(1))
    print(increase_seven(-10))
    print(increase_seven(-11.0))


if __name__ == "__main__":
    main()
