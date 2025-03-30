# https://pynative.com/python-json-exercise/
import json

input_dict = """{
   "company":{
      "employee":{
         "name":"emma",
         "payble":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


def convert_str_to_dict(test_str):
    print(type(test_str))
    test_json = json.loads(test_str)
    return test_json


def convert_dict_to_json(test_dict):
    print(type(test_dict))
    print(test_dict)
    test_json = json.dumps(test_dict)
    return json.loads(test_json)


def main():
    print("Access the nested key ‘salary’ from the following JSON")
    result_str = convert_str_to_dict(input_dict)
    print(type(result_str))
    test_value2 = result_str["company"]["employee"]["payble"]["salary"]
    print(test_value2)
    result_json = convert_dict_to_json(result_str)
    print(type(result_json))
    test_value = result_json["company"]["employee"]["payble"]["salary"]
    print(test_value)
    assert test_value == 7000


if __name__ == "__main__":
    main()
