import json

test_data = {
    "id": 10,
    "active": True,
    "age": 51,
    "name": "Сергей",
    "city": "Malaga",
    "borders": [23, 121, "18years"],
}


def main():
    print(json.dumps(test_data, sort_keys=True, indent=4, ensure_ascii=True))
    print(json.dumps(test_data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
