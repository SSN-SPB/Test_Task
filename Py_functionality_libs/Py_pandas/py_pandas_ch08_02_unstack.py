#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


# https://www.linkedin.com/learning/pandas-essential-training/reshaping?u=2113185
# stack


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from openpyxl.workbook import Workbook

# import xlsxwriter


print(pd.__version__)


def main():

    # skiprows - number of rows in csv file that should be skipped for DataFrame
    oo = pd.read_csv("./csv_data/Olympics2.csv", skiprows=4)
    # print(oo.head())

    oo_temp = oo[(oo.Edition == 2008) & ((oo.Event == "100m") | (oo.Event == "200m"))]
    print(oo_temp)
    oo_temp2 = oo_temp.groupby(["NOC", "Gender", "Discipline", "Event"]).agg(
        {"Event": "count"}
    )
    print(oo_temp2)
    g = oo_temp2.unstack(["Discipline", "Event"])
    print(g)
    # response
    #                Event
    # Discipline Athletics
    # Event           100m 200m
    # NOC Gender
    # JAM Men          1.0  1.0
    #     Women        3.0  2.0
    # TRI Men          1.0  NaN
    # USA Men          1.0  2.0
    #     Women        NaN  1.0
    # print(g.unstack())- transponse
    print("g.unstack()")
    print(g.unstack())
    # response


#                    Event
# Discipline Athletics
# Event           100m       200m
# Gender           Men Women  Men Women
# NOC
# JAM              1.0   3.0  1.0   2.0
# TRI              1.0   NaN  NaN   NaN
# USA              1.0   NaN  2.0   1.0


def back_up():
    print("backup")


if __name__ == "__main__":
    main()
