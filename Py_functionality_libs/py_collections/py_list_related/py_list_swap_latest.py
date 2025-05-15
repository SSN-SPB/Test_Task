def swapList(newList):
    size = len(newList)
    newList[0], newList[size - 1] = (
        newList[size - 1],
        newList[0],
    )
    return newList


newList = [12, 35, 9, 56, 25]

print(swapList(newList))


def main():
    new_swapped_list = swapList(newList)
    print(new_swapped_list)


if __name__ == "__main__":
    main()
