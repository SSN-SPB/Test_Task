#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


import pandas as pd

# read scv file to dataframe


print(pd.__version__)


def main():
    # oo = pd.read_csv('../csv_data2/Olympics2.csv', skiprows=4)
    oo = pd.read_json("C:\\Users\\Sergei_Smirnov\\Downloads\\jdiLightTemplate.json")
    ## print(oo.head())
    print(oo)
    print(type(oo))


if __name__ == "__main__":
    main()
