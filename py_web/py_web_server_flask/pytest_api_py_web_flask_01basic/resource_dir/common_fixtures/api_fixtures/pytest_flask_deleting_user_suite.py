from py_web.py_web_server_flask.pytest_api_py_web_flask_01basic.resource_dir import resourse_data
from py_web.py_web_server_flask.pytest_api_py_web_flask_01basic.resource_dir.requests import adding_user, get_page_data, deleting_user_by_id
from py_web.py_web_server_flask.pytest_api_py_web_flask_01basic.resource_dir.users_data import NEW_USER
import pytest


TESTED_PAGE = "api/users"
ENV_URL = resourse_data.BASE_URL
ENDPOINT = ENV_URL + TESTED_PAGE
print(ENDPOINT)


# @pytest.fixture
def add_user(request):
    """The method adds user"""
    response_code, response_message = adding_user(
        endpoint=ENDPOINT,
        user_city=NEW_USER["city"],
        user_email="test_201_" + NEW_USER["email"],
        first_name=NEW_USER["name"],
        last_name="test_201_" + NEW_USER["last_name"],
    )
    yield response_message['UserID']




