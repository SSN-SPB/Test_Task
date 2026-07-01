
import requests
import json
from jsonschema import validate, ValidationError
import sys

# tr3 =

# noinspection LanguageDetectionInspection
tr2 = {
    "mts": [
        {
            "index": 1,
            "name": "XCAL",
            "mobile": [
                {
                    "index": 1,
                    "phone_number": "7892208843",
                    "imsi": "***********8843"
                },
                {
                    "index": 2,
                    "phone_number": "7892208846",
                    "imsi": "***********8846"
                },
                {
                    "index": 3,
                    "phone_number": "7892208897",
                    "imsi": "***********8897"
                },
                {
                    "index": 4,
                    "phone_number": "7892208849",
                    "imsi": "***********8849"
                }
            ]
        }
    ]
}


xcal_mobile_info_schema = {
    "type": "object",
    "properties": {
        "mts": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "index": {"type": "integer"},  # mismatch: response has int
                    "name": {"type": "string","const": "XCAL"},
                    "mobile": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "index": {"type": "integer"},
                                "phone_number": {"type": "string",
                                                 "pattern": "^[0-9]{10}$"},
                                "imsi": {"type": "string","pattern": "^[*]{11}[0-9]{4}$"}
                            },
                            "required": ["index", "phone_number", "imsi"],
                            "additionalProperties": False,
                        },
                    },
                },
                "required": ["index", "name", "mobile"],
                "additionalProperties": False,
            },
        }
    },
    # "required": ["mts"],
    "required": ["mts"],
    "additionalProperties": False,
}


def main():
    try:
        validate(instance=tr2, schema=xcal_mobile_info_schema)
        print("Response matches schema")
        assert True
    except ValidationError as e:
        print(f"Schema validation failed: {e.message}")
        assert False


if __name__ == "__main__":
    main()
