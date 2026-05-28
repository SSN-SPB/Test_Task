from datetime import datetime


def get_current_datetime(date_format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Returns the current date and time formatted according to the specified format."""
    return datetime.now().strftime(date_format)


get_current_datetime_schema = {
    "name": "get_current_datetime",
    "description": "Returns the current date and time formatted according to the specified format",
    "input_schema": {
        "type": "object",
        "properties": {
            "date_format": {
                "type": "string",
                "description": "A string specifying the format of the returned datetime. Uses Python's strftime format codes.",
                "default": "%Y-%m-%d %H:%M:%S",
            }
        },
        "required": [],
    },
}


def process_tool_call(tool_name: str, tool_input: dict) -> str:
    if tool_name == "get_current_datetime":
        date_format = tool_input.get("date_format", "%Y-%m-%d %H:%M:%S")
        return get_current_datetime(date_format)
    raise ValueError(f"Unknown tool: {tool_name}")
