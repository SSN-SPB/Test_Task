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
# skiprows - number of rows in csv file that should be skipped for DataFrame
oo = pd.read_csv('./csv_data/Olympics2.csv', skiprows=4)
# print(oo.head())

def main():


# def tmm():
    oo_temp = oo[(oo.Edition == 2008)]

#def tmm():
    oo_temp2 = oo_temp.groupby(['NOC', 'Medal']).size().unstack('Medal',fill_value=0)
    print(oo_temp2)
    g=oo_temp2.sort_values(['Gold','Silver','Bronze'],\
                           ascending=False)[['Gold','Silver','Bronze']]
    print(g.head(7))
    g.head(7).plot(kind='bar')
    plt.show()
    g = g.transpose()
    print(g)
    sns.heatmap(g)
    plt.show()
    #changing plotsize
    plt.figure(figsize=(16,5))
    sns.heatmap(g)
    plt.show()
    
if __name__ == '__main__': main()
