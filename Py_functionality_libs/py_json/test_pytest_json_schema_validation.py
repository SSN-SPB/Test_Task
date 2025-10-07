import pytest
from jsonschema import validate, ValidationError

response = {
    "fns": [
        {
            "index": 1,
            "name": "TESTName",
            "mobile": [{"index": 1}, {"index": 2}, {"index": 3}, {"index": 4}],
        }
    ]
}


report_schema = {
    "type": "object",
    "properties": {
        "fns": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "index": {"type": "integer"},  # mismatch: response has int
                    "name": {"type": "string"},
                    "mobile": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {"index": {"type": "integer"}},
                            "required": ["index"],
                            "additionalProperties": False,
                        },
                    },
                },
                "required": ["index", "name", "mobile"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["fns"],
    "additionalProperties": False,
}


@pytest.mark.schema
def test_assert_scema():

    validate(instance=response, schema=report_schema)
    # assert reports_kpi_response.status_code == 200
    # assert login_response.json()["token"]
