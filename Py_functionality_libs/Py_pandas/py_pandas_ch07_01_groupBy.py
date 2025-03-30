#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


# https://www.linkedin.com/learning/pandas-essential-training/groupby?u=2113185
# 01 creeating group
# Split DataFrame to group by critera
# Apply a function to each group
# Combine the result into a DataFrame
# 02 iterate by group
# print(key)
# print(group)
# 03 groupby
# GroupBy.size()/GroupBy.count()/GroupBy.max()/GroupBy.min()
# agg() - aggregate multiple statistic
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

    oo2 =oo[(oo.Edition < 1988)]

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
