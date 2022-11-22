#!/usr/bin/env python3
import json
import requests
import pytest
from resource_dir import resourse_data


TESTED_PAIR = 'USDRUB'
MULTI_PAIR = 'USDRUB,AUDUSD,EURGBP'
ENV_URL = resourse_data.BASE_URL
ENDPOINT = ENV_URL + TESTED_PAIR
MULTI_ENDPOINT = ENV_URL + MULTI_PAIR


@pytest.fixture()
def expected_code():
    return {'OK': 200, 'NotKnownPair': 1002}


def get_pair_data(endpoint):
    get_request = requests.get(endpoint,
                               headers={'Content-Type': 'application/json'})
    requested_data = json.loads(get_request.text)
    return requested_data


@pytest.mark.check_negative
def test_negative_no_pair(expected_code):
    tested_response = get_pair_data(ENV_URL)
    checked_value_code = tested_response['code'] == expected_code['OK']
    checked_value_rates = tested_response['rates'] is None
    print('The code = 200 is: {}'.format(checked_value_code))
    print('The rates is: {}'.format(tested_response['rates']))
    assert checked_value_code
    assert checked_value_rates


@pytest.mark.check_negative
def test_code_unknown_pair_request(expected_code):
    tested_response = get_pair_data(ENV_URL + 'bad_endpoint_string')
    checked_value = tested_response['code'] == expected_code['NotKnownPair']
    print('The bad code = {} is: {}'.format(expected_code['NotKnownPair'],
                                            checked_value))
    assert checked_value


def test_usd_rub_rate_less_100():
    tested_response = get_pair_data(ENDPOINT)
    checked_value = tested_response['rates']['USDRUB']['rate'] < 100
    print('The ruble rate < 100 is: {}'.format(checked_value))
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
