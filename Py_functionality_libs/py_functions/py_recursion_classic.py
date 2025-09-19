def recursion_sum_plus_n(n, number):
    if n == 0:
        return 100
    else:
        print("new iteration")
        print(f"n - {n}, result - {number + recursion_sum_plus_n(n-1, number)}")
        return number + recursion_sum_plus_n(n-1, number)


def main():
    x = recursion_sum_plus_n(7, 3)
    print(x)


if __name__ == "__main__":
    main()
