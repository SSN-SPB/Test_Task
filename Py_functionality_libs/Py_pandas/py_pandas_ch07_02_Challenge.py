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
################ Challenge 1: Number of medal at each OG
    print ('Number of medal at each OG')
    fn = oo.groupby('Edition').size()
    print(fn)


################ Challenge 2 List of total medal for each county showing
################ the first and the latest OG
    print ('List of total medal for each county'
           ' showing the first and the latest OG')
    fn = oo.groupby('NOC').agg({'Edition': ['min','max','count']})
    print(fn)
    
if __name__ == '__main__': main()
