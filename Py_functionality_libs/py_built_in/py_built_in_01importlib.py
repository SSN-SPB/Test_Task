# This program demonstrates how to import via
# library in Python and use some of its functions.


def main():
    import importlib

    module = importlib.import_module("math")
    global module2
    module2 = importlib.import_module("math")
    print(module.sqrt(16))


if __name__ == "__main__":
    main()
    print(module2.sqrt(25))
