#!/usr/bin/env python3
import requests


def main():
    r = requests.get("https://medium.com/@pythonians")
    print(r.status_code)
    print(r.content)
    print(r.encoding)
    print(r.text)
    try:
        print(r.json())
    except Exception as e:
        print("No JSON found. See message: {}".format(e))
    print(r.headers)
    print(r.headers["Date"])
    for x, y in r.headers.items():
        print("{} is: {}".format(x, y))


if __name__ == "__main__":
    main()
