# This program demonstrates how to import a built-in
# library in Python and use some of its functions.


def main():
    math = __import__("math")
    print(math.sqrt(16))
    print(math.pi)


if __name__ == "__main__":
    main()
