def factorial(counter):
    if counter == 0:
        return 1
    return counter * factorial(counter - 1)


def main():
    print(factorial(5))
    # print(factorial(1))


if __name__ == "__main__":
    main()
