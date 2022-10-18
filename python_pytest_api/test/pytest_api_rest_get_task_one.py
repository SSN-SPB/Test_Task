#!/usr/bin/env python3
import json
import requests
import pytest


TESTED_PAIR = 'USDRUB'
ENV_URL = 'https://www.freeforexapi.com/api/live?pairs='
ENDPOINT = ENV_URL + TESTED_PAIR


@pytest.fixture()
def expected_code():
    return {'OK': 200, 'NotKnownPair': 1002}


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


@pytest.mark.check_response_code
def test_code_is_200(expected_code):
    tested_response = get_pair_data(ENDPOINT)
    checked_value = tested_response['code'] == expected_code['OK']
    print('The code = 200 is: {}'.format(checked_value))
    assert checked_value


@pytest.mark.check_response_code
def test_code_unknown_pair_request(expected_code):
    tested_response = get_pair_data(ENV_URL + 'bad_endpoint_string')
    checked_value = tested_response['code'] == expected_code['NotKnownPair']
    print('The bad code = {} is: {}'.format(expected_code['NotKnownPair'],
                                            checked_value))
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


if __name__ == '__main__':
    main()
