# json.loads() method is used to parse a JSON string and convert it
# into a Python object.
# It takes a JSON-formatted string as input and returns
# the corresponding Python object representation of that string.


import json

tested_json_string = (
    '{"id": 10, "active": true, "age": 91, "city": "Malaga", "activity": 15}'
)
EXPECTED_DICTIONARY = {
    "ID": 10,
    "ACTIVE": True,
    "AGE": 91,
    "CITY": "Malaga",
    "ACTIVITY": 15,
}


def convert_keys_to_upper_case(data):
    return {key.upper(): value for key, value in data.items()}


def check_json_loads_object_hook(json_string: str):
    return json.loads(json_string, object_hook=convert_keys_to_upper_case)


def main():
    result = check_json_loads_object_hook(tested_json_string)
    print(f"returned {result}")
    assert type(result) is dict
    assert result == EXPECTED_DICTIONARY


if __name__ == "__main__":
    main()
