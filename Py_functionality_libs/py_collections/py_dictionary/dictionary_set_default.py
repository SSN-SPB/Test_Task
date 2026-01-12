test_dict = {}


def main():
    print("The original dictionary is: " + str(test_dict))

    # Sort Dictionary key and values List
    # Using loop + dictionary comprehension
    test_dict.setdefault("users", [])
    # test_dict.setdefault("users", []).append("tom")

    # printing results
    for k, v in test_dict.items():
        print(f"The key: {k} has value {v}")
    test_dict.setdefault("users", []).append("tom")
    test_dict.setdefault("users", []).append("tom3")
    test_dict.setdefault("ages", []).append("28")
    test_dict.setdefault("ages", []).append("21")

    # printing results
    for k, v in test_dict.items():
        print(f"The key: {k} has value {v}")


if __name__ == "__main__":
    main()
