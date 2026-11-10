# json.loads() method is used to parse a JSON string and convert it
# into a Python object.
# It takes a JSON-formatted string as input and returns
# the corresponding Python object representation of that string.


import json

tested_json_string = (
    '{"id": 10, "active": true, "age": 91, "city": "Malaga", "activity": 15}'
)
EXPECTED_LIST = [
    ("id", 10),
    ("active", True),
    ("age", 91),
    ("city", "Malaga"),
    ("activity", 15),
]


def convert_keys_to_upper_case(data):
    return {key.upper(): value for key, value in data.items()}


def check_json_loads_object_pairs_hook(json_string: str):
    return json.loads(
        json_string,
        object_hook=convert_keys_to_upper_case,
        object_pairs_hook=list,
    )


def main():
    result = check_json_loads_object_pairs_hook(tested_json_string)
    print(f"returned {result}")
    assert type(result) is list
    assert result == EXPECTED_LIST


if __name__ == "__main__":
    main()
