import requests


def get_user(user_id: int):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()
