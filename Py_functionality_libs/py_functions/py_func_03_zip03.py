# zip() function in Python takes iterables (can be zero or more),
# aggregates them in a tuple, and returns it.
# if zip is used with *args, it can be used to unzip the list.


def main():
    tested_list = [[1, 2, 3], [21, 22, 33], [31, 32, 43]]
    mapped = list(zip(*tested_list))
    print(f"Result from zip: {mapped}")


if __name__ == "__main__":
    main()
