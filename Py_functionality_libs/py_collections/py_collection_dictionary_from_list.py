names = {"John", "Alexey", "Alima"}
names2 = {"John", "Alexey", "Alima", 777777}


def main():
    length_of_names = {name: len(name) for name in names}
    types_names = {name: type(name) for name in names2}
    print(length_of_names)
    print(types_names)


if __name__ == "__main__":
    main()
