def sum_of_kwargs(**kwargs):
    return sum(kwargs.values())


def main():
    print(sum_of_kwargs(list=1, pages=17, words=293))


if __name__ == "__main__":
    main()
