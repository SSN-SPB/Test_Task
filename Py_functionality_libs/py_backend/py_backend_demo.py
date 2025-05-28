#!/usr/bin/env python3


# import pytest
import requests

# https://requests.readthedocs.io/en/master/
# https://requests.readthedocs.io/en/master/api/#main-interface


def test_app_is_available(url="https://restful-booker.herokuapp.com/booking"):
    response = requests.get(url)
    print(response)
    # print(response.status_code)
    # print(list(response))
    assert response.ok
    return response


def test_page_unavailable():
    response = requests.get("https://restful-booker.herokuapp.com/not_there.html")
    assert response.status_code == 404


def main():
    rslt = test_app_is_available()  # <Response [200]>
    print(rslt.status_code)  # 200
    print(list(rslt))  # [b'[{"bookingid":1},{"bookingid":9},
    print(rslt.headers)

    test_page_unavailable()
    test_app_is_available("https://mail.ru")  # <Response [200]>
    print(rslt.headers)
    for k, v in rslt.headers.items():
        print("key is {} - value is {}".format(k, v))


if __name__ == "__main__":
    main()
