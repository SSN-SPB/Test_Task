def swap_values_via_lambda(x, y):
    swap = lambda x, y: (y, x)
    return swap(x, y)


def main():
    a, b = 5, 10
    print(f"init: a = {a}, b = {b}")

    # Use a lambda to swap their values
    swap = lambda x, y: (y, x)
    a, b = swap(a, b)
    print(f"swapped : a = {a}, b = {b}")

    print("a:", a)  # Output: a: 10
    print("b:", b)  # Output: b: 5

    a, b = swap_values_via_lambda(a, b)
    print(f"swapped back: a = {a}, b = {b}")


if __name__ == "__main__":
    main()
