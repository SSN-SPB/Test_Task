def main():
    new_dict = {}
    dict_keys = (1, 2, 3)
    new_dict[dict_keys] = "Value"
    print(new_dict)  # {(1, 2, 3): 'Value'}

    new_dict = {}
    dict_keys = [1, 2, 3]
    try:
        new_dict[dict_keys] = "Value"
    except TypeError as te:
        print("Dictionary can't be created:")
        print(te.args)
    print(new_dict)  # {}


if __name__ == "__main__":
    main()
