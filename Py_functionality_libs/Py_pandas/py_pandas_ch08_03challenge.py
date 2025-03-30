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

    
    # skiprows - number of rows in csv file that should be skipped for DataFrame
    oo = pd.read_csv('./csv_data/Olympics2.csv', skiprows=4)
    # print(oo.head())

# Challenge 1:
# plot number of gold medal by US male and Femail through the history
    oo_temp =oo[(oo.NOC == 'USA') & (oo.Medal == 'Gold')]
    print(oo_temp)
# def tmm():
    oo_temp2 = oo_temp.groupby(['Edition','Gender']).size()
    print(oo_temp2)
# def tmm():
    oo_temp2.plot (kind = 'bar',figsize=(15,6))
    plt.show()
# def tmm():
    oo_temp2 = oo_temp.groupby(['Edition','Gender']).size()\
    .unstack('Gender', fill_value=0)
    print(oo_temp2)
# def tmm():
    oo_temp2.plot (kind = 'line',figsize=(15,6))
    plt.show()
    oo_temp2.plot (kind = 'bar',figsize=(15,6))
    plt.show()
    # New view - unstacked Edition - moved to columns
    oo_temp2 = oo_temp.groupby(['Edition','Gender']).size()\
    .unstack('Edition', fill_value=0)
    print(oo_temp2)

def main2():
# Challenge 2:
# plot 5 athletes who won the most Gold medal in history

# plot number of gold medal by US male and Femail through the history
# def tmm():
    oo_temp2 = oo.groupby(['Athlete', 'Medal']).size()
    print(oo_temp2)

# def tmm():
    oo_temp2 = oo.groupby(['Athlete', 'Medal']).size().unstack('Medal',fill_value=0)
    print(oo_temp2)
    g=oo_temp2.sort_values(['Gold','Silver','Bronze'],\
                           ascending=False)[['Gold','Silver','Bronze']]
    print(g.head(7))
    g.head(7).plot(kind='bar')
    plt.show()
    
    
#if __name__ == '__main__': main()
if __name__ == '__main__': main2()
