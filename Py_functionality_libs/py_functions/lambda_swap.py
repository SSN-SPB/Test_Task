def main():
    a, b = 5, 10

    # Use a lambda to swap their values
    swap = lambda x, y: (y, x)
    a, b = swap(a, b)

    print("a:", a)  # Output: a: 10
    print("b:", b)  # Output: b: 5


if __name__ == "__main__":
    main()
