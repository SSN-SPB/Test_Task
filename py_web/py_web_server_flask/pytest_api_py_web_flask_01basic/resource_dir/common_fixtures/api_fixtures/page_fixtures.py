import pytest
from py_web.py_web_server_flask.pytest_api_py_web_flask_01basic.resource_dir.requests import \
    get_page_data
from py_web.py_web_server_flask.pytest_api_py_web_flask_01basic.resource_dir.resourse_data import (
    BASE_URL, HEALTH_PAGE)

HEALTH_PAGE_ENDPOINT = BASE_URL + HEALTH_PAGE


@pytest.fixture(scope="class")
def health_response(request):
    return get_page_data(HEALTH_PAGE_ENDPOINT)
