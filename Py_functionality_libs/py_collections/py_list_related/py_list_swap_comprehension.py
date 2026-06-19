# list comprehension is a concise way to create lists in Python.
# It allows you to generate a new list by applying
# an expression to each item in an existing
# iterable (like a list, tuple, or string)
# and optionally filtering the items based
# on a condition.



tested_list = [12, 35, 9, 56, 25]



def main():
    new_list = [x - 5 for x in tested_list]
    print(f"initial list: {tested_list}")
    print(f"updated list: {new_list}")


if __name__ == "__main__":
    main()
