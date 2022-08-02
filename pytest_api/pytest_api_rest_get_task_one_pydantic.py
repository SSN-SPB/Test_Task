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


def test_code_exists():
    tested_response = get_pair_data(ENDPOINT)
    checked_value = 'code' in tested_response.keys()
    print('The {} exists in response is: {}'.format('code', checked_value))
    assert checked_value


def test_rates_exists():
    tested_response = get_pair_data(ENDPOINT)
    checked_value = 'rates' in tested_response.keys()
    print('The {} exists in response is: {}'.format('rates', checked_value))
    assert checked_value


def test_code_is_200():
    tested_response = get_pair_data(ENDPOINT)
    checked_value = tested_response['code'] == 200
    print('The code = 200 is: {}'.format(checked_value))
    assert checked_value


def test_usrub_rate_less_100():
    tested_response = get_pair_data(ENDPOINT)
    checked_value = tested_response['rates']['USDRUB']['rate'] < 100
    print('The rate < 100 is: {}'.format(checked_value))
    assert checked_value


def main():
    retrieved_data = get_pair_data(ENDPOINT)
    print(retrieved_data)
    test_code_exists()
    test_rates_exists()
    test_code_is_200()
    test_usrub_rate_less_100()
    print('The validating response by pydantic')
    try:
        validated_responce = Response(**retrieved_data)
        print('The validating response by pydantic has passed')
    except BaseException as be:
        print('The unexpected format according to pydantic checking')


if __name__ == '__main__':
    main()
