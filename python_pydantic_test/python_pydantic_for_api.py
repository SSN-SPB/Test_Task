#!/usr/bin/env python3
import json
from msilib.schema import Error
import requests
from pydantic import BaseModel


TESTED_PAIR = 'USDRUB'
ENV_URL = 'https://www.freeforexapi.com/api/live?pairs='
ENDPOINT = ENV_URL + TESTED_PAIR


class Response(BaseModel):
    rates: dict
    code: int


def get_pair_data(endpoint):
    get_request = requests.get(endpoint,
                               headers={'Content-Type': 'application/json'})
    requested_data = json.loads(get_request.text)
    return requested_data


def main():
    retrieved_data = get_pair_data(ENDPOINT)
    print(retrieved_data)
    print('The validating response by pydantic')
    try:
        validated_responce = Response(**retrieved_data)
        print('The validating response by pydantic has passed')
    except BaseException as be:
        print('The unexpected format according to pydantic checking')


if __name__ == '__main__':
    main()
