import sys

arr_1 = []
arr_2 = arr_1


def main():
    print(sys.getrefcount(arr_1))
    print(arr_1)
    print(arr_2)
    print(dir(sys))
    print(sys.getsizeof(arr_1))
    print(sys.gettrace)


if __name__ == "__main__":
    main()
