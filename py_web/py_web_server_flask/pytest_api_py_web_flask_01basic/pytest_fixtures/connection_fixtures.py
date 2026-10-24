import pytest
from ..resource_dir.requests import get_page_data

pytest.fixture(scope="class")


def users_response(request):
    endpoint = request.cls.ENDPOINT
    return get_page_data(endpoint)
