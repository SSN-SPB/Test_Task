# json.loads() method is used to parse a JSON string and convert it
# into a Python object.
# It takes a JSON-formatted string as input and returns
# the corresponding Python object representation of that string.


import json

tested_json_string = (
    '{"id": 10, "active": true, "age": 91, "city": "Malaga", "activity": 15}'
)


def check_json_loads(json_string: str):
    return json.loads(json_string)


def main():
    result = check_json_loads(tested_json_string)
    print(f"returned {result}")
    assert isinstance(result, dict)


if __name__ == "__main__":
    main()
