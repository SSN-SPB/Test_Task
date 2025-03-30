newList = [12, 35, 9, "56z", 25]


def main():
    try:
        print(sum(newList))
    except TypeError as te:
        print(te)
    print("length of list is {}".format(sum(1 for i in newList)))


if __name__ == "__main__":
    main()
