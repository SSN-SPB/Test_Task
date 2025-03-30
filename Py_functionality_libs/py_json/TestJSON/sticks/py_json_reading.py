#!/usr/bin/env python3

import os
import json

# https://compscicenter.ru/courses/python/2015-autumn/classes/1388/


def main():
    with open("winedata_2.json") as file_1, open("winedata_2_copy.json", "w") as file_2:
        file_2.write(file_1.read())
    with open("winedata_2_copy.json", "r") as f:
        datastore = json.load(f)
    with open("winedata_1.json", "r") as f1:
        datastore_init = json.load(f1)
    number_of_records = 0
    for p in datastore:
        if p["points"] == "90":
            print("Points: " + p["points"])
            print("Title: " + p["title"])
            number_of_records = number_of_records + 1
            print("")
        # number_of_records = number_of_records + 1
    print("Total number of records is: {}".format(number_of_records))

    print(datastore == datastore_init)

    # l = json.dumps(datastore, indent=4)
    # print(l)


if __name__ == "__main__":
    result = main()
