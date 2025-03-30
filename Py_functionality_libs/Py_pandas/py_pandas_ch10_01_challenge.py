#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov




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

#def tmm():
    oo_temp = oo[(oo.NOC == 'USA')]
    print (oo_temp.head(7))
    select_on = oo_temp.groupby(['Edition', 'Athlete','Sport','Medal']).size().unstack(['Medal'],fill_value=0)
    
    
    # print (select_on.sort_values())
    print (select_on)
    select_on['Total'] = select_on['Gold'] + select_on['Silver'] + select_on['Bronze']
    print (select_on)
    select_on.reset_index(inplace=True)
    for year,group in select_on.groupby('Edition'):
        print(group.sort_values(['Total'],ascending=False)[:1])
    # gy = select_on.sort_values(['Total'],ascending=False)
    # print (gy)

    tu =[group.sort_values(['Total'],ascending=False)[:1] \
         for year,group in select_on.groupby('Edition')]
    reslt = pd.DataFrame()
    for i in tu:
         reslt = tu.append(i)
    print('The final list is:\n')
    print(reslt)


    
if __name__ == '__main__': main()
