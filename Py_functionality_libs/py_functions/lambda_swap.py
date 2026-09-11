def swap_values_via_lambda(x, y):
    return (lambda x, y: (y, x))(x, y)


def main():
    a, b = 5, 10
    a1, b1 = 15, 110
    print(f"init: a = {a}, b = {b}")
    print(f"init: a1 = {a1}, b = {b1}")

    # Use a lambda to swap their values
    swap = lambda x, y: (y, x)
    a, b = swap(a, b)
    print(f"swapped : a = {a}, b = {b}")
    a1, b1 = swap(a1, b1)
    print(f"swapped : a1 = {a1}, b = {b1}")

    print("a:", a)  # Output: a: 10
    print("b:", b)  # Output: b: 5

    a, b = swap_values_via_lambda(a, b)
    print(f"swapped back: a = {a}, b = {b}")


if __name__ == "__main__":
    main()
