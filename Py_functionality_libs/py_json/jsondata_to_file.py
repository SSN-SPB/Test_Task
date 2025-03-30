import json

data_json = {"name": "Sergei", "lastname": "Smirnov"}


def load_to_file(data):
    with open("data_json.txt", "w") as file:
        json.dump(data, file)


def load_from_file():
    f = open("data_json.txt")

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    for i in data:
        print(i)
        print(data[i])

    # Closing file
    f.close()


def main():
    load_to_file(data_json)
    load_from_file()


if __name__ == "__main__":
    main()
