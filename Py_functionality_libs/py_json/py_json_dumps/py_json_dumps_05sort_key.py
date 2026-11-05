import json

test_data = {
    "id": 10,
    "active": True,
    "age": 91,
    "city": "Malaga",
    "borders": [23, 121, "18years"],
}


def main():
    prepared_json_string = json.dumps(test_data, sort_keys=True, indent=4)
    print(prepared_json_string)


if __name__ == "__main__":
    main()
