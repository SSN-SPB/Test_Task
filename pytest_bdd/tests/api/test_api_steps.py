import requests
from pytest_bdd import scenarios, given, when, then

scenarios("../../pytest_bdd/features/api_login.feature")


BASE_URL = "https://www.freeforexapi.com/api/live?pairs="


@given("the API is available")
def api_available():
    response = requests.get(f"{BASE_URL}USDRUB")
    assert response.status_code == 200


@when("the response contains the expected fields")
def test_rates_exists():
    tested_response = requests.get(
        f"{BASE_URL}USDRUB", headers={"Content-Type": "application/json"}
    )
    checked_value = "code" in tested_response.json().keys()
    print("The {} exists in response is: {}".format("rates", checked_value))
    assert checked_value


@then("the code is more than 100")
def test_code_more_then_hundred():
    tested_response = requests.get(
        f"{BASE_URL}USDRUB", headers={"Content-Type": "application/json"}
    )
    checked_value = tested_response.json().get("code") > 100
    print("The {} exists in response is: {}".format("rates", checked_value))
    assert checked_value


# @when("I send login request with valid credentials")
# def send_login_request(context):
#     payload = {
#         "email": "eve.holt@reqres.in",
#         "password": "cityslicka"
#     }
#     context["response"] = requests.post(f"{BASE_URL}/login", json=payload)
#
# @then("the response status code should be 200")
# def verify_status_code(context):
#     assert context["response"].status_code == 200
#
# @then("the response should contain an access token")
# def verify_token(context):
#     assert "token" in context["response"].json()
