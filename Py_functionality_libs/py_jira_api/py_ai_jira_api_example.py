import pytest
import requests
import requests_mock
from jira_api_client import JiraApiClient  # Assuming you have a Jira API client class

BASE_URL = "https://your-jira-instance.atlassian.net/rest/api/3"
API_TOKEN = "your_api_token"
EMAIL = "your_email@example.com"


@pytest.fixture
def jira_client():
    return JiraApiClient(base_url=BASE_URL, email=EMAIL, api_token=API_TOKEN)


def test_get_issue(jira_client):
    issue_key = "TEST-123"
    expected_response = {
        "id": "10001",
        "key": issue_key,
        "fields": {"summary": "Test issue", "description": "This is a test"},
    }

    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URL}/issue/{issue_key}", json=expected_response)
        response = jira_client.get_issue(issue_key)

        assert response == expected_response


def test_create_issue(jira_client):
    issue_data = {
        "fields": {
            "project": {"key": "TEST"},
            "summary": "New issue",
            "description": "Creating a test issue",
            "issuetype": {"name": "Task"},
        }
    }
    expected_response = {"id": "10002", "key": "TEST-124"}

    with requests_mock.Mocker() as m:
        m.post(f"{BASE_URL}/issue", json=expected_response, status_code=201)
        response = jira_client.create_issue(issue_data)

        assert response == expected_response


def test_get_issue_not_found(jira_client):
    issue_key = "TEST-999"

    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URL}/issue/{issue_key}", status_code=404)

        with pytest.raises(requests.exceptions.HTTPError):
            jira_client.get_issue(issue_key)


def test_create_issue_invalid_data(jira_client):
    issue_data = {}  # Missing required fields

    with requests_mock.Mocker() as m:
        m.post(f"{BASE_URL}/issue", status_code=400)

        with pytest.raises(requests.exceptions.HTTPError):
            jira_client.create_issue(issue_data)
