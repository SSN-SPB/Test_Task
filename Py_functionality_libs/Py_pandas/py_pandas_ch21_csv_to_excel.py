#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov

# indexing
# https://www.linkedin.com/learning/pandas-essential-training/index?u=2113185

import pandas as pd
import sys


import pandas as pd
import matplotlib.pyplot as plt

print(pd.__version__)


def main():
    # skiprows - number of rows in csv file that should be skipped for DataFrame
    oo = pd.read_csv("./csv_data/Olympics2.csv", skiprows=4)
    # oo.to_excel("data.xls", index=False)  # Save without index
    # pip install xlwt
    # pip install openpyxl
    # oo.to_excel("data.xls", index=False, engine="xlwt")
    oo.to_excel("data.xlsx")


if __name__ == "__main__":
    main()
