test_dict = {"gfg": [7, 6, 3], "is": [2, 10, 3], "best": [19, 4]}


def main():
    print("The original dictionary is: " + str(test_dict))

    # Sort Dictionary key and values List
    # Using loop + dictionary comprehension
    res = dict()
    for key in sorted(test_dict):
        res[key] = sorted(test_dict[key])

    # printing results
    print("The sorted dictionary : " + str(res))


if __name__ == "__main__":
    main()
