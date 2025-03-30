#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


# https://www.linkedin.com/learning/pandas-essential-training/groupby?u=2113185
# DataFrame.groupby(agg([...]))
# DataFrame.groupby(agg({..:[...]}))



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from openpyxl.workbook import Workbook
# import xlsxwriter



print(pd.__version__)

def main():

    
    # skiprows - number of rows in csv file that should be skipped for DataFrame
    oo = pd.read_csv('./csv_data/Olympics2.csv', skiprows=4)
    # print(oo.head())



    # DataFrame.groupby(agg([...]))
    fn4 = oo.groupby(['Edition', 'NOC', 'Medal']).agg({'Edition':['min','max','count']})
    print(fn4)

    # agg({:[...]})
    fn = oo[oo.Athlete == 'LEWIS, Carl']
    print(fn)
    print ('oo[oo.Athlete == \'LEWIS, Carl\'].groupby(\'Athlete\')')
    fn = oo[oo.Athlete == 'LEWIS, Carl'].groupby('Athlete')
    print(type(fn))
    print(list(fn))

    print ('oo[oo.Athlete == \'LEWIS, Carl\'].groupby(\'Athlete\').agg({\'Edition\': [\'min\',\'max\',\'count\']')
    fn = oo[oo.Athlete == 'LEWIS, Carl'].groupby('Athlete').agg({'Edition': ['min','max','count']})
    print(type(fn))
    print(fn)


    print ('oo.groupby(\'Athlete\').agg({\'Edition\': [\'min\',\'max\',\'count\']')
    fn = oo.groupby('Athlete').agg({'Edition': ['min','max','count']})
    print(type(fn))
    print(fn)
    
if __name__ == '__main__': main()
