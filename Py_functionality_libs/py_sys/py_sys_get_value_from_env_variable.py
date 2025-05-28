#!/usr/bin/env python3

import os


def main_sys():
    user_name = os.environ.get("MYSQL_TEST_USER")
    password = os.environ.get("MYSQL_TEST_USER_PASS")
    print(user_name, password)
    # print(os.environ)


if __name__ == "__main__":
    main_sys()
