import pytest
from py_web.py_web_server_flask.pytest_api_py_web_flask_01basic.resource_dir.resourse_data import (
    RESPONSE_MESSAGES, USER_PAGE_ENDPOINT)

from ..resource_dir.requests import deleting_user_by_id, get_page_data


@pytest.mark.deleting_users
class TestClassDeletingUsersPage:

    def test_deleting_user_by_id(self):
        """Test checks the response code of deleting the last user"""
        _, initial_list = get_page_data(USER_PAGE_ENDPOINT)
        selected_id = initial_list[-1]["UserID"]
        deleting_response_code, deleting_response = deleting_user_by_id(
            USER_PAGE_ENDPOINT, selected_id
        )
        assert deleting_response_code == 200
        assert deleting_response["message"] == RESPONSE_MESSAGES[
            "SUCCESSFUL_DELETION_MESSAGE"
        ].format(selected_id)
