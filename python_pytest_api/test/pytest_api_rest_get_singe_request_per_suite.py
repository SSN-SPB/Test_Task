#!/usr/bin/env python3
from resource_dir import resourse_data
from resource_dir.requests import get_pair_data
import logging


class TestClass:

    TESTED_PAIR = 'USDRUB'
    ENV_URL = resourse_data.BASE_URL
    ENDPOINT = ENV_URL + TESTED_PAIR


tested_response = get_pair_data(TestClass.ENDPOINT)


def test_code_exists():
    checked_value = 'code' in tested_response.keys()
    logging.warning('The {} exists in response is: {}'.format('code', checked_value))
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
