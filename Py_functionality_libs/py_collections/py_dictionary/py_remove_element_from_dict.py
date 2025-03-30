def main():
    test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
    print(test_dict)

    # empty the dictionary d
    y = {}
    # eliminate the unrequired element
    for key, value in test_dict.items():
        if key != "Arushi":
            y[key] = value
    print(y)


if __name__ == "__main__":
    main()
