def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)


def main():
    print(mydoubler(12))
    print(mytripler(11))


if __name__ == "__main__":
    main()
