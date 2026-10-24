import pytest

from ..resource_dir import resourse_data
from ..resource_dir.requests import get_page_data
from ..service_data.pages_content import initial_users


@pytest.fixture(scope="class")
def users_response(request):
    endpoint = request.cls.ENDPOINT
    return get_page_data(endpoint)


class TestClassUsersPage:

    TESTED_PAGE = "/api/users"
    ENV_URL = resourse_data.BASE_URL
    ENDPOINT = ENV_URL + TESTED_PAGE

    def test_code_is_200(self, users_response):
        response_code, _ = users_response
        checked_value = response_code == 200
        print("The response code = 200 is: {}".format(checked_value))
        assert checked_value

    def test_users_are_returned(self, users_response):
        _, tested_response = users_response
        checked_value = tested_response == initial_users
        print(
            "The users response matches the expected data: {}".format(
                checked_value
            )
        )
        assert checked_value

    def test_number_of_initial_users(self, users_response):
        _, tested_response = users_response
        checked_value = len(initial_users) == 7
        print(
            "The users response matches the expected data: {}".format(
                checked_value
            )
        )
        assert checked_value
