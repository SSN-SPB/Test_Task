# https://pynative.com/python-json-exercise/
import json

input_dict = {"key12": "value1", "key11": "value2"}


def convert_dict_to_json(test_dict):
    print(type(test_dict))
    print(test_dict)
    test_json = json.dumps(test_dict)
    return json.loads(test_json)


def get_json_value_by_key(test_json, tesk_key):
    test_value = test_json[tesk_key]
    return test_value


def main():
    result_json = convert_dict_to_json(input_dict)
    print(result_json)
    print(type(result_json))
    expected_value = get_json_value_by_key(result_json, "key12")
    print(expected_value)
    print(type(result_json))
    pretty_json = json.dumps(result_json, indent=2, separators=(",", " = "))
    print(pretty_json)
    print(type(pretty_json))
    print("Exercise 4: Sort JSON keys in and write them into a file")
    file_name_modified = open("file_to_modify.txt", "w+")
    interim_list = []
    for k, v in result_json.items():
        interim_list.append(k)
    print(interim_list)
    interim_list.sort()
    for x in interim_list:
        print(x)
        file_name_modified.write(x + "\n")


if __name__ == "__main__":
    main()
