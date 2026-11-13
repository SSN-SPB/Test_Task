import json
from uuid import uuid4
from pathlib import Path

response_data = {"status_code": 201, "time": "21 june", "status": "success"}
current_mark = str(uuid4())[:8]


def dump_file(delete_created=False):
    print(f"tested uuid: {current_mark}")
    with open(f"response_{current_mark}.json", "w") as response_file:
        json.dump(response_data, response_file, indent=4, sort_keys=True)
    current_list = [file.name for file in Path(".").glob("*.json")]
    print(current_list)
    for x in current_list:
        print(x)
    if delete_created:
        for x in Path(".").glob("*.json"):
            x.unlink()
            print(f"Deleted file {x}")
        current_list = [file.name for file in Path(".").glob("*.json")]
        assert len(current_list) == 0


def ramp_down(file_name):
    Path(file_name.name).unlink()
    print(f"Deleted file {Path(file_name.name)}")


def main():
    dump_file(delete_created=False)
    with open(f"response_{current_mark}.json", "r") as checked_file:
        t = json.load(checked_file)
        print(t)
        assert type(t) is dict
    ramp_down(checked_file)


if __name__ == "__main__":
    main()
