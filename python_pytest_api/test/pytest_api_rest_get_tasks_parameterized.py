#!/usr/bin/env python3
import json
import requests
import pytest


ENV_URL = 'https://www.freeforexapi.com/api/live?pairs='
RESPONSE_CODE_LIST = [
    ("USDRUB", 200),
    ("EURUSD,USDRUB", 200),
    ("NOT_EXISTING_PAIR", 1002)
    ]


def get_pair_data(endpoint):
    get_request = requests.get(endpoint,
                               headers={'Content-Type': 'application/json'})
    requested_data = json.loads(get_request.text)
    return requested_data


@pytest.mark.check_response_code
@pytest.mark.parametrize("pair_to_check, expected_code", RESPONSE_CODE_LIST)
def test_different_codes_parametrized_checking(pair_to_check, expected_code):
    tested_response = get_pair_data(ENV_URL + pair_to_check)
    checked_value = tested_response['code'] == expected_code
    print('The code = {} for pair {} is: {}'
          .format(expected_code, pair_to_check, checked_value))
    assert checked_value
