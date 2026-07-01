# Initializing lists for keys and values

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
name = ["Jan", "Feb", "March"]


def make_dict(keys, values):
    """Function to create dictionary from 2 lists"""
    return dict(zip(keys, values))


def main():
    result_dict = make_dict(months, name)
    print(f"Flattened dictionary is: {result_dict}")


if __name__ == "__main__":
    main()
