import requests

BASE_URL = "https://web-test-python-smirnov6-g0dsfyhwbpbfe5b5.spaincentral-01.azurewebsites.net"

# Test GET
r = requests.get(BASE_URL)
print(r.text)

# Test POST
payload = {"name": "Sergei", "msg": "Hello cloud!"}
r = requests.post(f"{BASE_URL}/api/echo", json=payload)

print(r.json())