import json

import requests


def get_page_data(endpoint):
    get_request = requests.get(
        endpoint, headers={"Content-Type": "application/json"}
    )
    requested_data = json.loads(get_request.text)
    return get_request.status_code, requested_data


def adding_user(endpoint, user_city, user_email, first_name, last_name):
    add_user = requests.post(
        endpoint,
        headers={"Content-Type": "application/json"},
        json={
            "city": user_city,
            "email": user_email,
            "first_name": first_name,
            "last_name": last_name,
        },
    )

    adding_user_response = json.loads(add_user.text)
    return add_user.status_code, adding_user_response


def deleting_user_by_id(endpoint, user_id):
    delete_user = requests.delete(
        endpoint + "/" + str(user_id),
        headers={"Content-Type": "application/json"},
    )

    deleting_user_response = json.loads(delete_user.text)
    return delete_user.status_code, deleting_user_response
