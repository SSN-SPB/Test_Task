def swapList(newList):
    size = len(newList)
    newList[0], newList[size - 1] = newList[size - 1], newList[0],
    return newList


newList = [12, 35, 9, 56, 25]

print(swapList(newList))


def main():
    swapList(newList)


if __name__ == "__main__":
    main()
