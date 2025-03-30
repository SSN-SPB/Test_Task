def main():
    coordinates = (3, 4)
    my_dict = {coordinates: "Point A"}

    print(my_dict[coordinates])

    try:
        coordinates2 = (3, [4])
        my_dict2 = {coordinates2: "Point A"}

        print(my_dict2[coordinates])
    except TypeError as te:
        print(te)


if __name__ == "__main__":
    main()