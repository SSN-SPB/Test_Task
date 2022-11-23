#!/usr/bin/env python3
import pytest
from resource_dir import resourse_data
from resource_dir.requests import get_pair_data

TESTED_PAIR = 'EURUSD,USDRUB'
TESTED_PAIR_WITH_EMPTY_COMMA_INSIDE = 'EURUSD,,,USDRUB'
ENV_URL = resourse_data.BASE_URL
ENDPOINT = ENV_URL + TESTED_PAIR
ENDPOINT_WITH_EMPTY_COMMAS = ENV_URL + TESTED_PAIR_WITH_EMPTY_COMMA_INSIDE


def test_code_is_200():
    tested_response = get_pair_data(ENDPOINT)
    checked_value = tested_response['code'] == 200
    print('The code = 200 is: {}'.format(checked_value))
    assert checked_value


def test_euro_usd_rate_exists():
    tested_response = get_pair_data(ENDPOINT)
    checked_value = 'EURUSD' in tested_response['rates'].keys()
    print('The EURUSD exists in response is: {}'.format(checked_value))
    assert checked_value


@pytest.mark.check_different_version_of_pairs
def test_internal_comma_doesnt_affect_response():
    tested_response = get_pair_data(ENDPOINT)
    tested_response2 = get_pair_data(ENDPOINT_WITH_EMPTY_COMMAS)
    print('without commas: {}'.format(tested_response))
    print('with commas: {}'.format(tested_response2))
    checked_value = tested_response == tested_response2
    print('The commas inside request do'
          ' not affect response is: {}'.format(checked_value))
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
    test_euro_usd_rate_exists()
    test_usdrub_exists()


if __name__ == '__main__':
    main()
