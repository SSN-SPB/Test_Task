#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


import pandas as pd

# read scv file to dataframe


print(pd.__version__)


def main():
    # oo = pd.read_csv('./csv_data/Olympics2.csv', skiprows=4)
    # skiprows - number of rows in csv file that should be skipped for DataFrame
    oo = pd.read_csv("./csv_data/Olympics2.csv", skiprows=4)
    print("head of dataframe:")
    print(oo.head())
    print("oo as it is {}".format(oo))

    print(oo)
    print(type(oo))
    print("print(oo['City'])")
    print(oo["City"])
    print("print(oo.City)")
    print(type(oo.City))  #
    print(oo.City)  # if no spaces in Serie
    print("print(oo[['City','Event']])")
    print(type(oo[["City", "Event"]]))
    print(oo[["City", "Event"]])
    print("print(oo['NOC'])")
    print(type(oo["NOC"]))
    print(oo["NOC"])
    print(oo.NOC)


if __name__ == "__main__":
    main()
