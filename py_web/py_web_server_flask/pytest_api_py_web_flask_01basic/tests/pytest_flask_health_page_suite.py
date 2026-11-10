import pytest
from py_web.py_web_server_flask.pytest_api_py_web_flask_01basic.resource_dir.common_fixtures.api_fixtures.page_fixtures import \
    health_response


@pytest.mark.health_page
class TestClassHealthPage:

    def test_code_is_200(self, health_response):
        response_code, _ = health_response
        assert response_code == 200

    def test_status_ok(self, health_response):
        _, tested_response = health_response
        assert tested_response["status"] == "ok"

    def test_service_name(self, health_response):
        _, tested_response = health_response
        assert tested_response["service"] == "flask-training"
