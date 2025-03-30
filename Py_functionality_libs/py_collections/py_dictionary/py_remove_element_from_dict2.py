def main():
    test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
    # Using pop() to remove a dict. pair
    # removes Mani
    removed_value = test_dict.pop("Mani")

    # Printing dictionary after removal
    print("The dictionary after remove is : " + str(test_dict))
    print("The removed key's value is : " + str(removed_value))


if __name__ == "__main__":
    main()
