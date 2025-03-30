def main():
    a, b, c = 1, 2, 3
    print("a = {}, b = {}, c = {}".format(a, b, c))  # a = 1, b = 2, c = 3
    a, b = "35"
    print("a = {}, b = {}".format(a, b))  # a = 3, b = 5
    a, *b = 1, 2, 3
    print("a = {}, b = {}".format(a, b))  # a = 1, b = [2, 3]
    a, *b, c = 7, 1, 2, 3
    print("a = {}, b = {}, c = {}".format(a, b, c))  # a = 7, b = [1, 2], c = 3
    a, _, c = 1, 2, 3
    print("Missed b: a = {}, _ = {}, c = {}".format(a, _, c))
    # a = 1, b = 2, c = 3
    print("Missed b2: a = {}, c = {}".format(a, c))  # a = 1, b = 2, c = 3
    a, b, c = [4, 5, 6]
    print(
        "from list: a = {}, b = {}, c = {}".format(a, b, c)
    )  # from list: a = 4, b = 5, c = 6
    a, b, c = (9, 5, 6)
    print(
        "from cortege: a = {}, b = {}, c = {}".format(a, b, c)
    )  # from list: from cortege: a = 9, b = 5, c = 6
    a, b, c = range(42, 45)
    print(
        "from range: a = {}, b = {}, c = {}".format(a, b, c)
    )  # from range: a = 42, b = 43, c = 44


if __name__ == "__main__":
    main()
