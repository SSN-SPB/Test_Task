#!/usr/bin/env python3
import json
import requests


TESTED_PAIR = 'STABILNOST'
ENV_URL = 'https://www.freeforexapi.com/api/live?pairs='
ENDPOINT = ENV_URL + TESTED_PAIR
ERROR_MESSAGE = 'was not recognised or supported'


def get_pair_data(endpoint):
    get_request = requests.get(endpoint,
                               headers={'Content-Type': 'application/json'})
    requested_data = json.loads(get_request.text)
    return requested_data


def test_message_contains_error_text():
    tested_response = get_pair_data(ENDPOINT)
    checked_value = ERROR_MESSAGE in tested_response['message']
    print('The message contains error message is: {}'.format(checked_value))
    assert checked_value


def test_supportedpairs_exists():
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
    retrieved_data = get_pair_data(ENDPOINT)
    test_message_contains_error_text()
    test_supportedpairs_exists()
    test_code_is_1002()


if __name__ == '__main__':
    main()