#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov

# sort indexing
# https://www.linkedin.com/learning/pandas-essential-training/using-sort-index?u=2113185
import pandas as pd
import sys


import pandas as pd
import matplotlib.pyplot as plt

print(pd.__version__)

def main():
    # skiprows - number of rows in csv file that should be skipped for DataFrame
    oo = pd.read_csv('./csv_data/Olympics2.csv', skiprows=4)
    print(oo.head())
    print(oo.index)
    ath = oo.set_index('Athlete')
    print(ath.head())
    ath.sort_index(inplace = True)
    print(ath.head())
    ath.sort_index(inplace = True,ascending = False)
    print(ath.head())


    
if __name__ == '__main__': main()
