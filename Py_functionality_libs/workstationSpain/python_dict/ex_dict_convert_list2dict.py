# https://pynative.com/python-tuple-exercise-with-solutions/
keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]


def convert_list_to_dict(test_keys: "list()", test_values: "list") -> dict:
    final_dict = dict()
    for x in test_keys:
        final_dict.update({x: test_values[test_keys.index(x)]})
    return final_dict


def main():
    print(convert_list_to_dict(keys, values))
    assert convert_list_to_dict(keys, values) == {"Ten": 10, "Twenty": 20, "Thirty": 30}


if __name__ == "__main__":
    main()
