from ..resource_dir import resourse_data
from ..resource_dir.requests import get_page_data
import logging


class TestClassHealthPage:

    TESTED_PAGE = "/api/health"
    ENV_URL = resourse_data.BASE_URL
    ENDPOINT = ENV_URL + TESTED_PAGE


# response_code, tested_response = get_page_data(TestClassHealthPage.ENDPOINT)


def _test_code_exists():
    checked_value = "code" in tested_response.keys()
    logging.warning(
        "The {} exists in response is: {}".format("code", checked_value)
    )
    assert checked_value


def test_code_is_200():
    response_code, tested_response = get_page_data(TestClassHealthPage.ENDPOINT)
    checked_value = response_code == 200
    print("The response code = 200 is: {}".format(checked_value))
    assert checked_value


def test_status_ok():
    response_code, tested_response = get_page_data(TestClassHealthPage.ENDPOINT)
    checked_value = tested_response["status"] == "ok"
    print("The key {} has value ok - is: {}".format("status", checked_value))
    assert checked_value


def test_service_name():
    response_code, tested_response = get_page_data(TestClassHealthPage.ENDPOINT)
    checked_value = tested_response["service"] == "flask-training"
    print(
        "The key {} has value flask-training - is: {}".format(
            "service", checked_value
        )
    )
    assert checked_value
