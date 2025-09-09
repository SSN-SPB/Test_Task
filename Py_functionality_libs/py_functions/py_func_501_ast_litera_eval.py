import ast

list_string = "[24, 1, 4, 2, 9, 17, 27, 37, 47, 57]"
dict_string = '{1: "peanut", 2: "butter", 3: "jelly", 4: "time"}'


def main():
    result_list = ast.literal_eval(list_string)
    assert result_list == [24, 1, 4, 2, 9, 17, 27, 37, 47, 57]
    result_dict = ast.literal_eval(dict_string)
    assert result_dict == {1: "peanut", 2: "butter", 3: "jelly", 4: "time"}


if __name__ == "__main__":
    main()
