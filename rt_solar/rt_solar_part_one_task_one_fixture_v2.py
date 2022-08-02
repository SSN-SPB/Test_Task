#!/usr/bin/env python3
import json
import requests


class TestClass:

    TESTED_PAIR = 'USDRUB'
    ENV_URL = 'https://www.freeforexapi.com/api/live?pairs='
    ENDPOINT = ENV_URL + TESTED_PAIR


def get_pair_data(endpoint):
    get_request = requests.get(endpoint,
                               headers={'Content-Type': 'application/json'})
    requested_data = json.loads(get_request.text)
    return requested_data


tested_response = get_pair_data(TestClass.ENDPOINT)


def test_code_exists():
    checked_value = 'code' in tested_response.keys()
    print('The {} exists in response is: {}'.format('code', checked_value))
    assert checked_value


def test_rates_exists():
    checked_value = 'rates' in tested_response.keys()
    print('The {} exists in response is: {}'.format('rates', checked_value))
    assert checked_value


def test_code_is_200():
    checked_value = tested_response['code'] == 200
    print('The code = 200 is: {}'.format(checked_value))
    assert checked_value


def test_usrub_rate_less_100():
    checked_value = tested_response['rates']['USDRUB']['rate'] < 100
    print('The rate < 100 is: {}'.format(checked_value))
    assert checked_value
