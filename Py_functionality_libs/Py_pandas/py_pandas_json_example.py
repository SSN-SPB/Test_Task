#!/usr/bin/env python3
# This code demonstrates how to read a JSON file into
# a pandas DataFrame and display its contents.
# It uses the `pd.read_json()` function to load the data and then
# prints the first few rows, the entire DataFrame, and its type.


import pandas as pd


print(pd.__version__)


def main():
    json = "simple_for_pandas.json"
    oo = pd.read_json("%s" % json)
    print(oo.head())
    print(oo)
    print(type(oo))


if __name__ == "__main__":
    main()
