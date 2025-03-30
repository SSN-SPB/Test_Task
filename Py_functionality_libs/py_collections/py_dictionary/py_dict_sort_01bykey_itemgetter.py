from operator import itemgetter

dict1 = {"a": 10, "b": 8}
dict2 = {"d": 6, "c": 4}
# Initializing list of dictionaries
list_of_dict = [
    {"name": "Nandini", "age": 20},
    {"name": "Manjeet", "age": 27},
    {"name": "Tom", "age": 27},
    {"name": "Adams", "age": 27},
    {"name": "Nikhil", "age": 19},
]


def sort_list_of_dict(tested_list, key_value):
    sorted_list = sorted(tested_list, key=itemgetter(key_value))
    return sorted_list


def main():
    result_list = sort_list_of_dict(list_of_dict, "age")
    print(result_list)


if __name__ == "__main__":
    main()
