# https://www.tutorialstonight.com/python/pattern-program-in-python#square-pattern
size = 5


def main():
    for i in range(0, size):
        # Create a list of columns
        for j in range(0, size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    main()
