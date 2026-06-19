import requests


def get_user(user_id):
    response = requests.get(
        f"https://api.example.com/users/{user_id}"
    )

    if response.status_code == 200:
        return response.json()

    return None