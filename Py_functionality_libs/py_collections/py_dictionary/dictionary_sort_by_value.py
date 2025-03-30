test_dict = {"gfg": [7, 6, 3], "is": [2, 10, 3], "best": [19, 4]}


def main():
    print("The original dictionary is: " + str(test_dict))

    # Sort Dictionary key and values List
    # Using loop + dictionary comprehension
    res = sorted(test_dict.items(), key=lambda x: x[1])

    # printing results
    print("The sorted dictionary : " + str(res))


if __name__ == "__main__":
    main()
