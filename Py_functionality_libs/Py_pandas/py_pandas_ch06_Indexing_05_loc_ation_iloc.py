#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov

# loc[] ation
# htttps://www.linkedin.com/learning/pandas-essential-training/using-loc?u=2113185
import pandas as pd
import sys


import pandas as pd
import matplotlib.pyplot as plt

print(pd.__version__)


def main():
    # skiprows - number of rows in csv file that should be skipped for DataFrame
    oo = pd.read_csv("./csv_data/Olympics2.csv", skiprows=4)
    print(oo.head())
    # print(oo.index)
    oo.set_index("Athlete", inplace=True)
    print(oo.head())
    print("print(oo.loc['MALOKINIS, Ioannis'])")
    print(oo.loc["MALOKINIS, Ioannis"])

    print("print(oo.loc['BOLT, Usain'])")
    print(oo.loc["BOLT, Usain"])

    # resetting the index
    print("resetting the index")
    oo.reset_index(inplace=True)
    print(oo.head())

    ath = oo[oo.Athlete == "BOLT, Usain"]
    print("ath = oo[oo.Athlete == 'BOLT, Usain'], print ath.head()")
    print(ath.head())

    ath = oo.loc[oo.Athlete == "BOLT, Usain"]
    print("ath = oo.loc[oo.Athlete == 'BOLT, Usain'], print ath.head()")
    print(ath.head())


if __name__ == "__main__":
    main()
