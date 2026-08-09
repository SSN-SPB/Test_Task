def factorial_via_recursion(n: int):
    if n == 0:
        return 1
    return n * factorial_via_recursion(n - 1)


def starting_code(n):
    for i in range(0, n):
        print(f"factorial for {i} is {factorial_via_recursion(i)}")


if __name__ == "__main__":
    starting_code(5)
