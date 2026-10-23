import pytest

from ..resource_dir import resourse_data
from ..resource_dir.requests import get_page_data


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
        expected_users = [
            {
                "City": "New York",
                "Email": "john.smith@email.com",
                "FirstName": "John",
                "LastName": "Smith",
                "UserID": 1,
            },
            {
                "City": "Chicago",
                "Email": "emma.johnson@email.com",
                "FirstName": "Emma",
                "LastName": "Johnson",
                "UserID": 2,
            },
            {
                "City": "Dallas",
                "Email": "michael.brown@email.com",
                "FirstName": "Michael",
                "LastName": "Brown",
                "UserID": 3,
            },
            {
                "City": "Seattle",
                "Email": "sophia.davis@email.com",
                "FirstName": "Sophia",
                "LastName": "Davis",
                "UserID": 4,
            },
            {
                "City": "Boston",
                "Email": "james.wilson@email.com",
                "FirstName": "James",
                "LastName": "Wilson",
                "UserID": 5,
            },
            {
                "City": "Austin",
                "Email": "olivia.taylor@email.com",
                "FirstName": "Olivia",
                "LastName": "Taylor",
                "UserID": 6,
            },
            {
                "City": "Denver",
                "Email": "daniel.anderson@email.com",
                "FirstName": "Daniel",
                "LastName": "Anderson",
                "UserID": 7,
            },
        ]
        _, tested_response = users_response
        checked_value = tested_response == expected_users
        print(
            "The users response matches the expected data: {}".format(
                checked_value
            )
        )
        assert checked_value
