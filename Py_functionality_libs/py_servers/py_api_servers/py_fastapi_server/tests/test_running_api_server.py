import httpx

BASE_URL = "http://127.0.0.1:8000"


def test_server_is_running():
    try:
        response = httpx.get(f"{BASE_URL}/", timeout=2.0)
    except httpx.ConnectError:
        assert False, "FastAPI server is NOT running"

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


def test_read_item_live():
    response = httpx.get(f"{BASE_URL}/items/5")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5}
