#!/usr/bin/env python3
import pytest
from resource_dir import resourse_data
from resource_dir.requests import get_pair_data


ENV_URL = resourse_data.BASE_URL


RESPONSE_CODE_LIST = [
    ("USDRUB", 200),
    ("EURUSD,USDRUB", 200),
    ("NOT_EXISTING_PAIR", 1002)
    ]


@pytest.mark.check_response_code
@pytest.mark.parametrize("pair_to_check, expected_code", RESPONSE_CODE_LIST)
def test_different_codes_parametrized_checking(pair_to_check, expected_code):
    tested_response = get_pair_data(ENV_URL + pair_to_check)
    checked_value = tested_response['code'] == expected_code
    print('The code = {} for pair {} is: {}'
          .format(expected_code, pair_to_check, checked_value))
    assert checked_value
