def main():
    print(dir(zip))
    name = ["Orange", "Apple", "Orange", "Plump", "Plump", "Grape", "Apple"]
    roll = [4, 1, 4, 2, 9, 17, 27, 37, 47, 57]
    roll_string = ["a", "b", "a", "s"]
    small_roll = list(range(20, 2, -2))
    print(small_roll)

    # using zip() to map values
    mapped = zip(name, roll)
    mapped2 = zip(name, small_roll)
    print(dict(mapped))
    print(list(mapped2))

    print(set(mapped))
    print(list(mapped))  # []
    mapped = zip(name, roll)
    print(list(mapped))
    print(name)
    print(list(mapped))  # []
    print("name one more time {}".format(name))

    # Three lists
    mapped3 = zip(name, roll, roll_string)
    print(list(mapped3))
    print(list(mapped3))
    mapped4 = zip(name, roll, roll_string)
    print(set(mapped4))
    mapped5 = zip(name, roll)
    print(dict(mapped5))


if __name__ == "__main__":
    main()
