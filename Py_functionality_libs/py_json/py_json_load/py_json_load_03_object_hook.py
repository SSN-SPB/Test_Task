# json.load() method is used to parse a JSON file and
# convert it into a Python object.
# json.load(object_hook=...) allows you to specify
# a custom function (object_hook)
# that will be called for each JSON object during the parsing process.
# This function can be used to modify or transform the parsed objects
# before they are returned as Python objects.


import json
import logging
from pathlib import Path
from uuid import uuid4

response_data = {
    "status_code": 201,
    "time": f"21 june {uuid4()}",
    "status": "success",
}
current_mark = str(uuid4())[:8]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def dump_file(delete_created=False):
    logger.info(f"tested uuid: {current_mark}")
    with open(f"response_{current_mark}.json", "w") as response_file:
        json.dump(response_data, response_file, indent=4, sort_keys=True)
    current_list = [file.name for file in Path(".").glob("*.json")]
    logger.info(current_list)
    for x in current_list:
        logger.info(x)
    if delete_created:
        for x in Path(".").glob("*.json"):
            x.unlink()
            logger.info(f"Deleted file {x}")
        current_list = [file.name for file in Path(".").glob("*.json")]
        assert len(current_list) == 0


def convert_keys_to_upper(data):
    return {key.upper(): value for key, value in data.items()}


def deleting_file_by_name(file_name):
    Path(file_name.name).unlink()
    logger.info(f"Deleted file {Path(file_name.name)}")


def main():
    dump_file(delete_created=False)
    with open(f"response_{current_mark}.json", "r") as checked_file:
        t = json.load(checked_file, object_hook=convert_keys_to_upper)
        logger.info(t)
        logger.info(t.keys())
        logger.info(list(t.keys())[0])
        assert type(t) is dict
        assert list(t.keys())[0] == "STATUS"
    deleting_file_by_name(checked_file)


if __name__ == "__main__":
    main()
