import pytest

from ..resource_dir import resourse_data
from ..resource_dir.requests import get_page_data

@pytest.fixture(scope="class")
def health_response(request):
    endpoint = request.cls.ENDPOINT
    return get_page_data(endpoint)


class TestClassHealthPage:

    TESTED_PAGE = "/api/health"
    ENV_URL = resourse_data.BASE_URL
    ENDPOINT = ENV_URL + TESTED_PAGE

    def test_code_is_200(self, health_response):
        response_code, tested_response = health_response
        checked_value = response_code == 200
        print("The response code = 200 is: {}".format(checked_value))
        assert checked_value

    def test_status_ok(self, health_response):
        response_code, tested_response = health_response
        checked_value = tested_response["status"] == "ok"
        print(
            "The key {} has value ok - is: {}".format("status", checked_value)
        )
        assert checked_value

    def test_service_name(self, health_response):
        response_code, tested_response = health_response
        checked_value = tested_response["service"] == "flask-training"
        print(
            "The key {} has value flask-training - is: {}".format(
                "service", checked_value
            )
        )
        assert checked_value
