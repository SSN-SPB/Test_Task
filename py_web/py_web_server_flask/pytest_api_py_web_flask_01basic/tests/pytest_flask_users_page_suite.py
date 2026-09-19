from ..resource_dir import resourse_data
from ..resource_dir.requests import get_page_data


class TestClassUsersPage:

    TESTED_PAGE = "/api/users"
    ENV_URL = resourse_data.BASE_URL
    ENDPOINT = ENV_URL + TESTED_PAGE


# response_code, tested_response = get_page_data(TestClassUsersPage.ENDPOINT)


def test_code_is_200():
    response_code, tested_response = get_page_data(TestClassUsersPage.ENDPOINT)
    checked_value = response_code == 200
    print("The response code = 200 is: {}".format(checked_value))
    assert checked_value


def test_users_are_returned():
    expected_users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"},
        {"id": 3, "name": "Robert"},
    ]
    response_code, tested_response = get_page_data(TestClassUsersPage.ENDPOINT)
    checked_value = tested_response == expected_users
    print("The users response matches the expected data: {}".format(checked_value))
    assert checked_value
