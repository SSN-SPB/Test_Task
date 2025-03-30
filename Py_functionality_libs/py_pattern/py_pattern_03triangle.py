# https://www.tutorialstonight.com/python/pattern-program-in-python#square-pattern
size = 5


def main():
    for i in range(0, size):
        # Create a list of columns
        for j in range(0, size):
            if j <= i:
                print('*', end='')
        print()


if __name__ == "__main__":
    main()
