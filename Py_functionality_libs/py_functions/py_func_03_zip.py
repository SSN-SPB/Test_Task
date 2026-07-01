def main():
    # print(dir(zip))
    list_of_string = ["Orange", "Apple", "Orange", "Plump", "Plump", "Grape", "Apple"]
    roll = [4, 1, 4, 2, 9, 17, 27, 37, 47, 57]
    roll_string = ["a", "b", "a", "s"]
    small_list = list(range(20, 2, -2))
    print(small_list)

    # using zip() to map values
    mapped = zip(list_of_string, roll)
    mapped2 = zip(list_of_string, small_list)
    print(f"Dict from zip: {dict(mapped)}")
    print(f"list from zip: {list(mapped2)}")
    print(f"list from zip: {list(zip(list_of_string, small_list))}")
    print(f"Dict from zip: {dict(zip(list_of_string, small_list))}")
    print(f"Set from zip: {set(zip(list_of_string, small_list))}")

    # print(list(mapped2))
    #
    # print(set(mapped))
    # print(list(mapped))  # []
    # mapped = zip(list_of_string, roll)
    # print(list(mapped))
    # print(list_of_string)
    # print(list(mapped))  # []
    # print("list_of_string one more time {}".format(list_of_string))
    #
    # # Three lists
    # mapped3 = zip(list_of_string, roll, roll_string)
    # print(list(mapped3))
    # print(list(mapped3))
    # mapped4 = zip(list_of_string, roll, roll_string)
    # print(set(mapped4))
    # mapped5 = zip(list_of_string, roll)
    # print(dict(mapped5))


if __name__ == "__main__":
    main()
