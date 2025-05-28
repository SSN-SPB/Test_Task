#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


import pandas as pd

# read scv file to dataframe
# shape
# head
# tail
# info


print(pd.__version__)


def main():
    # oo = pd.read_csv('./csv_data/Olympics2.csv', skiprows=4)
    # skiprows - number of rows in csv file that should be skipped for DataFrame
    oo = pd.read_csv("../csv_data2/Olympics2.csv", skiprows=4)
    # print(oo.shape)
    # print('oo.head()')
    # print(oo.head())
    # print('oo.tail()')
    # print(oo.tail())
    print("oo.tail(3)")
    print(oo.tail(3))
    # print('oo.tail(-15)')
    # print(oo.tail(-15))
    # print('oo.head(10)')
    # print(oo.head(10))
    # print('oo.head(-15)')
    # print(oo.head(-15))
    print("oo.info()")
    print(oo.info())


if __name__ == "__main__":
    main()
