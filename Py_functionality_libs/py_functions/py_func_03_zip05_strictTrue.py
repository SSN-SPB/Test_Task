# This script demonstrates the use of the zip() function
# with the strict parameter set to True.
# It shows how to handle cases where the input lists have different lengths,
# raising a ValueError when attempting to iterate over the zipped object.


list_one = [1, 2]
list_two = ["a", "b", "c"]


def zip_strict_test(test_list_one: list, test_list_two: list):
    try:
        new_zip = zip(test_list_one, test_list_two, strict=True)
    except ValueError:
        print("During creating iterator the exception is not raised")

    try:
        for k, v in new_zip:
            print(k, v)
    except ValueError as ve:
        print(f"The lists have different length:{ve}")


def main():
    zip_strict_test(test_list_one=list_one, test_list_two=list_two)


if __name__ == "__main__":
    main()
