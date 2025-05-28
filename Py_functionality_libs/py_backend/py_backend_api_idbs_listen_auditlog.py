#!/usr/bin/env python3


# import pytest
import urllib.request
import json
import requests

# https://www.w3schools.com/python/ref_requests_post.asp

USER_LOGIN = "sn2_qatestenv@idbs.com"
USER_PASSWORD = "supernova2_qa"
X_API = "7bRwIK19AALByHRv55g19lIJ7wwtNB"
SITE_URL = "https://pas-test-client.supernova-qa.idbs-ecs-dev.eworkbookcloud.com/login/default-qatestenv"
ENDD_POINT_URL = "https://audit-log-service.sn2-qa.supernova.eworkbookcloud.com/audit/api/v1/messages?"
ENDD_POINT_PARAM = "service=ADMIN_PORTAL&tenant=default-qatestenv&from=2020-12-16T15:00:00.000Z&to=2021-12-20T00:00:00.000Z&count=10"
ENDPOINT = ENDD_POINT_URL + ENDD_POINT_PARAM
# ENDPOINT = 'https://audit-log-service.sn2-qa.supernova.eworkbookcloud.com/audit/api/v1/messages?service=ADMIN_PORTAL&tenant=default-qatestenv&from=2020-12-16T15:00:00.000Z&to=2021-12-20T00:00:00.000Z&count=10'


def get_token(url, login, password, xAPI):

    response_text = requests.post(
        url,
        headers={"Content-Type": "application/json", "X-API-KEY": xAPI},
        json={
            "app": "ecs",
            "username": login,
            "password": password,
            "scopes": "platform-admin",
        },
    )

    token = json.loads(response_text.text)["access_token"]
    return token


def get_request(endpoint, token):
    get_iprange_text = requests.get(
        endpoint, headers={"Content-Type": "application/json", "Authorization": token}
    )
    ipranges_list = json.loads(get_iprange_text.text)
    return ipranges_list


def main():
    # input data
    url = SITE_URL
    get_endpoint = ENDPOINT
    xAPI = X_API
    login = (USER_LOGIN,)
    password = USER_PASSWORD

    # Getting token
    token_current = get_token(url, login, password, xAPI)
    # print('Requested current token is: ' + token_current)

    # getting token
    bear_token = "Bearer " + token_current

    print("----- The last message --------")
    last_message = get_request(get_endpoint, bear_token)["messages"][0]
    print(last_message)
    ## while
    while True:
        new_message = get_request(get_endpoint, bear_token)["messages"][0]
        if new_message != last_message:
            last_message = new_message
            print(last_message)


if __name__ == "__main__":
    main()
