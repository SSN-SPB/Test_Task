#!/usr/bin/env python3
import pytest
import allure
from resource_dir import resourse_data
from resource_dir.requests import get_pair_data


TESTED_PAIR = 'USDRUB'
MULTI_PAIR = 'USDRUB,AUDUSD,EURGBP'
ENV_URL = resourse_data.BASE_URL
ENDPOINT = ENV_URL + TESTED_PAIR
MULTI_ENDPOINT = ENV_URL + MULTI_PAIR


@pytest.fixture()
def expected_code():
    return {'OK': 200, 'NotKnownPair': 1002}

@allure.step("Example test with allur logging")
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


@pytest.mark.count_occurrences
def _test_count_occurrences_rates():
    tested_response = get_pair_data(MULTI_ENDPOINT)
    print('The multi response is: '.format(tested_response))
    c = 0
    for k, v in tested_response['rates'].items():
        for k1, v1 in v.items():
            if k1 == 'rate':
                print('The pair {} has rate {} '.format(k, v1))
                c = c + 1
    checked_value = c == len(tested_response['rates'])
    print('The occurrence rate checking is: {}'.format(checked_value))
    assert checked_value


def _test_usd_rub_rate_less_100():
    tested_response = get_pair_data(ENDPOINT)
    checked_value = tested_response['rates']['USDRUB']['rate'] < 100
    print('The ruble rate < 100 is: {}'.format(checked_value))
    assert checked_value
