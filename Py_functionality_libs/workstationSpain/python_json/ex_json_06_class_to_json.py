# https://pynative.com/python-json-exercise/
import json
from json import JSONEncoder

print("Access the nested key ‘salary’ from the following JSON")


def convert_dict_to_json(test_dict):
    test_json = json.dumps(test_dict)
    return json.loads(test_json)


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

result_dict = {"name": vehicle.name, "engine": vehicle.engine, "price": vehicle.price}

result_json = convert_dict_to_json(result_dict)
print(result_dict)
print(result_json)
print(type(result_json))
print(result_dict["name"])
print(result_json["name"])
pretty_json = json.dumps(result_dict, indent=2, separators=(",", " = "))
print(pretty_json)


class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


vehicleJson = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
print(vehicleJson)


list_of_attributes = []
for x in vehicle.__dict__:
    list_of_attributes.append(x)


new_dict = {}

for x in list_of_attributes:
    y = str(x)
    new_dict[x] = 2

print("new dict: {}".format(new_dict))
