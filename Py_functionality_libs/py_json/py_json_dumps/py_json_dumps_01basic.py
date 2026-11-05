# json.dumps() method is used to convert a Python object into a JSON string.
# It takes a Python object as input and returns a JSON-formatted string
# representation of that object.

import json

data = {"id": 10, "active": True}


def main():
    prepared_data = json.dumps(data)
    print(type(prepared_data))
    print(prepared_data)


if __name__ == "__main__":
    main()
