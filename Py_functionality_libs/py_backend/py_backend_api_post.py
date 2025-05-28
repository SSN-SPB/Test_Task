#!/usr/bin/env python3


# import pytest
import urllib.request
import json
import requests

# https://requests.readthedocs.io/en/master/
# https://requests.readthedocs.io/en/master/api/#main-interface
# https://www.w3schools.com/python/ref_requests_post.asp

USER_LOGIN = "sn2_qatestenv@idbs.com"
USER_PASSWORD = "supernova2_qa"
X_API = "7bRwIK19AALByHRv55g19lIJ7wwtNB"
SITE_URL = "https://pas-test-client.supernova-qa.idbs-ecs-dev.eworkbookcloud.com/login/default-qatestenv"
ENDPOINT = "https://ipconfig-service.sn2-qa.supernova.eworkbookcloud.com/ipconfig/api/v1/default-qatestenv/ipranges"


def get_token(url, login, password, xAPI):

    response_text = requests.post(
        url,
        headers={"Content-Type": "application/json", "X-API-KEY": xAPI},
        json={
            "app": "ecs",
            "username": login,
            "password": password,
            "scopes": "user-admin,eln,request",
            "pas_type": "ldap",
        },
    )
    token = json.loads(response_text.text)["access_token"]
    return token


def post_iprange(
    get_endpoint, bear_token, iprange, ip_descripton="Default description"
):

    request_body = {"cidr": iprange, "description": ip_descripton}

    post_iprange = requests.post(
        get_endpoint,
        json=request_body,
        headers={"Content-Type": "application/json", "Authorization": bear_token},
    )
    print("Adding range return code is {}".format(post_iprange))


def get_ipranges(endpoint, token):
    get_iprange_text = requests.get(
        endpoint, headers={"Content-Type": "application/json", "Authorization": token}
    )
    ranges_in_JSONformat = json.loads(get_iprange_text.text)
    return ranges_in_JSONformat


def get_ipranges_cidr(endpoint, token):
    get_ipranges(endpoint, token)
    cidr_list = []
    theJSONlist = get_ipranges(endpoint, token)
    for i in theJSONlist:
        print(i["cidr"])
        cidr_list.append(i["cidr"])
    return cidr_list


def add_new_range(get_endpoint, bear_token, iprange, ipdescription):
    list_of_cidrs = get_ipranges_cidr(get_endpoint, bear_token)
    if not (iprange in list_of_cidrs):
        post_iprange(get_endpoint, bear_token, iprange, ipdescription)
    else:
        print("Your {} is in list already".format(iprange))


def main():
    # input data
    url = SITE_URL
    get_endpoint = ENDPOINT
    xAPI = X_API
    login = (USER_LOGIN,)
    password = USER_PASSWORD

    # Getting token
    token_current = get_token(url, login, password, xAPI)
    print("Requested current token is: " + token_current)

    # getting token
    bear_token = "Bearer " + token_current
    theJSONformat = get_ipranges(get_endpoint, bear_token)
    # print(theJSONformat)
    total_records = 0
    print("List of ranges: ")
    for i in theJSONformat:
        total_records = total_records + 1
        print(i)
        print("-----")
        print(i["id"])
    print("Total number of records {}".format(total_records))
    print("----- All CIDRs --------")
    list_of_cidrs = get_ipranges_cidr(get_endpoint, bear_token)
    print(list_of_cidrs)
    print("0.0.0.0/0" in list_of_cidrs)
    add_new_range(get_endpoint, bear_token, "17.11.127.164/27", "Autotest")


if __name__ == "__main__":
    main()
