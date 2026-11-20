# Script to demonstrate the use of json.load() with object_pairs_hook
# to convert JSON objects into a list of key-value pairs.
# Pay attention that
# 1 the order of the key-value pairs is preserved in the resulting list.
# 2 object_hook=... is ignored when object_pairs_hook is provided.

import json
import logging
from pathlib import Path
from uuid import uuid4

current_mark = str(uuid4())[:8]
response_data = {
    "status_code": 201,
    "time": f"21 june {current_mark}",
    "status": "success",
}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s\t%(filename)s:%(lineno)d\t\t%(message)s",
)
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
        t = json.load(
            checked_file,
            object_hook=convert_keys_to_upper,
            object_pairs_hook=list,
        )
        logger.info(t)
        assert type(t) is list
        assert t[0][1] == "success"
        assert t == [
            ("status", "success"),
            ("status_code", 201),
            ("time", f"21 june {current_mark}"),
        ]
    deleting_file_by_name(checked_file)


if __name__ == "__main__":
    main()
