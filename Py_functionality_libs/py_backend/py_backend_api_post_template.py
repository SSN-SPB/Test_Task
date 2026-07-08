import requests

url = "https://api.example.com/v1/users"

headers = {"Authorization": "Bearer YOUR_API_KEY", "Content-Type": "application/json"}

payload = {"name": "John Doe", "email": "john@example.com", "age": 30}

try:
    response = requests.post(
        url,
        headers=headers,
        json=payload,  # Automatically serializes to JSON
        timeout=30,
    )

    # Raise an exception for HTTP errors (4xx/5xx)
    response.raise_for_status()

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
    print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
