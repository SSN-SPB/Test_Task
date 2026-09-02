def fibonacci(y):
    if y <= 1:
        return y
    else:
        interim = fibonacci(y - 1) + fibonacci(y - 2)
        # print(f"Count for {y} interim result is {interim}")
        return interim


def main():
    fibonacci_list = list()
    for x in range(10):
        fibonacci_list.append(fibonacci(x))

    print(fibonacci_list)


if __name__ == "__main__":
    main()
