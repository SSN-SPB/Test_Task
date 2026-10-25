from uuid import uuid4

import pytest

from ..resource_dir import resourse_data
from ..resource_dir.requests import adding_user, get_page_data

NEW_USER_UUID = str(uuid4())[0:8]
NEW_USER_CITY = f"CITY_{NEW_USER_UUID}"
NEW_USER_EMAIL = f"user.{NEW_USER_UUID}@email.com"
NEW_USER_NAME = f"user_name_{NEW_USER_UUID}"
NEW_USER_LAST_NAME = f"user_last_name_{NEW_USER_UUID}"


class TestClassAddingUsersPage:

    TESTED_PAGE = "/api/users"
    ENV_URL = resourse_data.BASE_URL
    ENDPOINT = ENV_URL + TESTED_PAGE

    def test_adding_user_code_is_201(self, request):
        """Test checks the response code of adding new user"""
        _, initial_list = get_page_data(request.cls.ENDPOINT)
        initial_list_length = len(initial_list)
        response_code, _ = adding_user(
            endpoint=request.cls.ENDPOINT,
            user_city=NEW_USER_CITY,
            user_email=NEW_USER_EMAIL,
            first_name=NEW_USER_NAME,
            last_name=NEW_USER_LAST_NAME,
        )
        checked_value = response_code == 201
        print("The response code = 201 is: {}".format(checked_value))
        _, modified_list = get_page_data(request.cls.ENDPOINT)
        modified_list_length = len(modified_list)
        assert checked_value
        assert initial_list_length + 1 == modified_list_length
