#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


# https://www.linkedin.com/learning/pandas-essential-training/creating-your-own-colormaps?u=2113185
# https://html-color-codes.info/


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from openpyxl.workbook import Workbook

# colormap import
from matplotlib.colors import ListedColormap


print(pd.__version__)
# skiprows - number of rows in csv file that should be skipped for DataFrame
oo = pd.read_csv("./csv_data/Olympics2.csv", skiprows=4)
# print(oo.head())


def main():

    # def tmm():
    oo_temp = oo  # [(oo.Edition == 2008)]

    # def tmm():
    oo_temp2 = (
        oo_temp.groupby(["Athlete", "Medal"]).size().unstack("Medal", fill_value=0)
    )
    print(oo_temp2)
    g = oo_temp2.sort_values(["Gold", "Silver", "Bronze"], ascending=False)[
        ["Gold", "Silver", "Bronze"]
    ]
    print(g.head(7))
    g.head(7).plot(kind="bar")
    plt.show()
    # print the curent colormap
    for x in list(sns.color_palette()):
        print(x)
    # display the curent colormap
    sns.palplot(sns.color_palette())
    plt.show()

    # setting new color palete
    gsb = ["#FFBF00", "#F2F2F2", "#61210B"]
    sns.palplot(sns.color_palette(gsb))
    plt.show()
    my_color = ListedColormap(sns.color_palette(gsb))
    g.head(8).plot(kind="bar", colormap=my_color)
    plt.show()


def tmm():
    g = g.transpose()
    print(g)
    sns.heatmap(g)
    plt.show()
    # changing plotsize
    plt.figure(figsize=(16, 5))
    sns.heatmap(g)
    plt.show()


if __name__ == "__main__":
    main()
