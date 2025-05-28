#!/usr/bin/env python3
import os
import time
import datetime


def print_all_variable():
    for a in os.environ:
        print("Var: ", a, "has value: ", os.getenv(a).split(";"))


def main():
    ts = time.time()
    dat = datetime.datetime
    time_stamp = dat.fromtimestamp(ts).strftime("%Y_%m_%d_%H_%M_%S")
    os.environ["dt"] = time_stamp
    print(os.getenv("dt"))
    print_all_variable()


if __name__ == "__main__":
    main()


def reserved_function():
    # Set environment variables
    os.environ["API_USER"] = "username"
    os.environ["API_PASSWORD"] = "secret"

    # Get environment variables
    USER = os.getenv("API_USER")
    PASSWORD = os.environ.get("API_PASSWORD")

    # Getting non-existent keys
    FOO = os.getenv("FOO")  # None
    BAR = os.environ.get("BAR")  # None
    BAZ = os.environ["BAZ"]  # KeyError: key does not exist.
