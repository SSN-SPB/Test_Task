from itertools import pairwise


def main2():
    list2 = [1, 2, 3, 6, 12]
    dict_test = dict()
    for a, b in pairwise(list2):
        print(f"{a}-{b}")
        dict_test[a] = b
    print(dict_test)



if __name__ == "__main__":
    main2()
