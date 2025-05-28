#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov

# iloc[] (index location)
# https://www.linkedin.com/learning/pandas-essential-training/using-iloc?u=2113185
import pandas as pd
import sys


import pandas as pd
import matplotlib.pyplot as plt

print(pd.__version__)


def main():
    # skiprows - number of rows in csv file that should be skipped for DataFrame
    oo = pd.read_csv("./csv_data/Olympics2.csv", skiprows=4)
    print(oo.head())
    print(oo.iloc[2:5])
    # it returns
    #      City  Edition     Sport  ...                       Event Event_gender   Medal
    # 2  Athens     1896  Aquatics  ...  100m freestyle for sailors            M  Bronze
    # 3  Athens     1896  Aquatics  ...  100m freestyle for sailors            M    Gold
    # 4  Athens     1896  Aquatics  ...  100m freestyle for sailors            M  Silver
    print(oo.iloc[[25, 11, 3000, 200]])


# it returns
#          City  Edition      Sport  ...         Event Event_gender   Medal
# 25     Athens     1896  Athletics  ...          800m            M  Silver
# 11     Athens     1896  Athletics  ...          100m            M  Bronze
# 3000  Antwerp     1920  Athletics  ...  110m hurdles            M  Silver
# 200     Paris     1900   Aquatics  ...    water polo            M    Gold

if __name__ == "__main__":
    main()
