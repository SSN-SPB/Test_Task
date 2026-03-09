# Initializing list of dictionaries
test_dict = {"month": [1, 2, 3, 4], "name": ["Jan", "Feb", "March"]}


def main():
    # printing original dictionary
    print("The original dictionary is : " + str(test_dict))

    # Convert key-values list to flat dictionary
    # Using dict() + zip()
    res = dict(zip(test_dict["month"], test_dict["name"]))

    # printing result
    print("Flattened dictionary is: {}".format(res))


if __name__ == "__main__":
    main()
