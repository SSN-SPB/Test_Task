from operator import *


def returnSum(dict):
    sum = 0
    for i in dict.values():
        sum = sum + i

    return sum


def main():
    result_sum = 0
    sum1 = sum(newList[::-1])
    print(sum1)
    for i in newList2:
        result_sum = add(i, result_sum)
    print(result_sum)


if __name__ == "__main__":
    main()
