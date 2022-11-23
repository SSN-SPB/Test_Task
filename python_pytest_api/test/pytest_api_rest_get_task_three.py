#!/usr/bin/env python3
from resource_dir import resourse_data
from resource_dir.requests import get_pair_data


TESTED_PAIR = 'NOT_EXISTING_PAIR'
ENV_URL = resourse_data.BASE_URL
ENDPOINT = ENV_URL + TESTED_PAIR
ERROR_MESSAGE = 'was not recognised or supported'


def test_message_contains_error_text():
    tested_response = get_pair_data(ENDPOINT)
    checked_value = ERROR_MESSAGE in tested_response['message']
    print('This message contains error message is: {}'.format(checked_value))
    assert checked_value


def test_response_text_contains():
    tested_response = get_pair_data(ENDPOINT)
    checked_value = 'supportedPairs' in tested_response.keys()
    print('The supportedPairs exists in response is: {}'.format(checked_value))
    assert checked_value


def test_code_is_1002():
    tested_response = get_pair_data(ENDPOINT)
    checked_value = tested_response['code'] == 1002
    print('The code = 1002 is: {}'.format(checked_value))
    assert checked_value


def main():
    test_message_contains_error_text()
    test_response_text_contains()
    test_code_is_1002()


if __name__ == '__main__':
    main()
