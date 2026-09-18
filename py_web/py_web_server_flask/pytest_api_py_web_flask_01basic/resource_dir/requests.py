import json
import requests


def get_page_data(endpoint):
    get_request = requests.get(
        endpoint, headers={"Content-Type": "application/json"}
    )
    requested_data = json.loads(get_request.text)
    return get_request.status_code, requested_data
