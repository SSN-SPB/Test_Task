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

def main():

    
    # skiprows - number of rows in csv file that should be skipped for DataFrame
    oo = pd.read_csv('./csv_data/Olympics2.csv', skiprows=4)
    # print(oo.head())

    oo_temp =oo[(oo.Edition == 2008) & ((oo.Event == '100m')|(oo.Event == '200m'))]
    print(oo_temp)
    oo_temp2 = oo_temp.groupby(['NOC','Gender','Discipline','Event']).agg({'Event':'count'})
    print(oo_temp2)
    g = oo_temp2.unstack(['Discipline','Event'])
    print(g)
    writer = pd.ExcelWriter('Unstacked_value.xlsx', engine = 'xlsxwriter')
    g.to_excel(writer, sheet_name='Unstacked')
    writer.save()
    writer.close()

    stacked_g = g.stack('Event')
    print('g.stacked(Event)')
    print(stacked_g)

    # Using


def back_up():    
### 01 creeating group
    list_edition = list(oo.groupby('Edition'))
    print ('groupBy list')
    print(list_edition)
    
# 02 iterate by group
    with pd.ExcelWriter('Medal_in_Each_olympic.xlsx') as writer:
        for group_key, group_value in oo2.groupby('Edition'):
            print('group_key: {}'.format(group_key))
            print('group_value type {}: value \n{}'.format(type(group_value),group_value))
            print(group_key)
            group_value.to_excel(writer, sheet_name=str(group_key))

# 03 groupby
    #SIZE
    print('SIZE: oo.groupby(\'Edition\').size()')
    print(oo.groupby('Edition').size())

    fn = oo.groupby(['Edition', 'NOC', 'Medal'])
    # too long
    # print(list(fn))
    fn2 = oo.groupby(['Edition', 'NOC', 'Medal']).agg(['min','max','count'])
    print(type(fn2)) # I is the DataFrame
    print('aggregated group value')
    print(fn2)
    writer2 = pd.ExcelWriter('AgregatedValues.xlsx', engine = 'xlsxwriter')
    fn2.to_excel(writer2, sheet_name='aggregationOne')

    # agg()
    print('simplified')
    fn2 = oo.groupby(['Edition', 'NOC', 'Medal']).agg('count')
    print(fn2)
    print('size only')
    fn3 = oo.groupby(['Edition', 'NOC', 'Medal']).size()
    print(fn3)
    fn3.to_excel(writer2, sheet_name='groupedByCountedMedal')

    writer2.save()
    writer2.close()

    
    
if __name__ == '__main__': main()
