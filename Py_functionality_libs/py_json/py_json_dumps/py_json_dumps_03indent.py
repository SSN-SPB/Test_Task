import json

test_data = {
    "id": 10,
    "active": True,
    "age": 91,
    "city": "Malaga",
    "activity": 15,
}


def main():
    prepared_json_string = json.dumps(test_data, indent=4)
    print(prepared_json_string)


if __name__ == "__main__":
    main()
