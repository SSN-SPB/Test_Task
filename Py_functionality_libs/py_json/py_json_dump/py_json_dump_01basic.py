# json.dump() function is used to write a Python object into a JSON file.
# It takes two arguments:
#   the Python object to be written
#   the file object where the JSON data will be stored.
# The function also has optional parameters such as:
#   indent
#   sort_keys,
# which can be used to format the output JSON data.

import json
from uuid import uuid4
from pathlib import Path

response_data = {"status_code": 201, "time": "21 june", "status": "success"}


def main():
    with open(f"response_{str(uuid4())[:8]}.json", "w") as response_file:
        json.dump(response_data, response_file, indent=4, sort_keys=True)
    for x in list(Path(".").glob("*.json")):
        print(x)


if __name__ == "__main__":
    main()
