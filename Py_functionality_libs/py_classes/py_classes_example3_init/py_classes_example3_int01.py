class Limit:
    def __int__(self):
        return 2


def main():
    limit = Limit()
    print(int(limit))
    print(limit)
    try:
        print("abcde"[:limit])
    except TypeError as te:
        print(te.__doc__)
        print(te)
    print("abcde"[: int(limit)])


if __name__ == "__main__":
    main()
