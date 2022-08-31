#!/usr/bin/env python3
import json
import requests


TESTED_PAIR = 'EURUSD,USDRUB'
ENV_URL = 'https://www.freeforexapi.com/api/live?pairs='
ENDPOINT = ENV_URL + TESTED_PAIR


def get_pair_data(endpoint):
    get_request = requests.get(endpoint,
                               headers={'Content-Type': 'application/json'})
    requested_data = json.loads(get_request.text)
    return requested_data


def test_code_is_200():
    tested_response = get_pair_data(ENDPOINT)
    checked_value = tested_response['code'] == 200
    print('The code = 200 is: {}'.format(checked_value))
    assert checked_value


def test_eurusd_exists():
    tested_response = get_pair_data(ENDPOINT)
    checked_value = 'EURUSD' in tested_response['rates'].keys()
    print('The EURUSD exists in response is: {}'.format(checked_value))
    assert checked_value


def test_usdrub_exists():
    tested_response = get_pair_data(ENDPOINT)
    checked_value = 'USDRUB' in tested_response['rates'].keys()
    print('The USDRUB exists in response is: {}'.format(checked_value))
    assert checked_value


def main():
    retrieved_data = get_pair_data(ENDPOINT)
    print(retrieved_data)
    test_code_is_200()
    test_eurusd_exists()
    test_usdrub_exists()


if __name__ == '__main__':
    main()
