# https://pynative.com/python-json-exercise/

input_list = [
    {"id": 1, "name": "name1", "color": ["red", "green"]},
    {"id": 2, "name": "name2", "color": ["pink", "yellow"]},
]

result_list = []


def main():
    for x in input_list:
        for k, v in x.items():
            if k == "name":
                print(v)
                result_list.insert(0, v)
    print(result_list)
    assert result_list == ["name2", "name1"]



if __name__ == "__main__":
    main()
