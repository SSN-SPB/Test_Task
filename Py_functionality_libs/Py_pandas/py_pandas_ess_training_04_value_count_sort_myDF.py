#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


import pandas as pd
# pandas version
# pandas value_count()
# pandas sort_values()



def main():
    series_index = list(range(2,16,2))
    age = [21, 41, 61, 71 , None,61, 38]
    first_name = ['John', 'Bill', 'Jimm', 'Jimm','Jordge', 'Jimm','Jimm']
    state = ['CO', 'AR', 'NY', 'CA', None, 'AR','MA']
    columns_data = ['Age', 'Name', 'State']

    # row data
    data_frame2 = (age,first_name,state)
    dataFrame2=pd.DataFrame(data_frame2)
   # transponse row data
    dataFrame2_1 = dataFrame2.transpose()
    # adding columns
    dataFrame2_1.columns = columns_data
    # addint indexes
    dataFrame2_1.index = series_index
    print(dataFrame2_1)
    print('dataFrame2_1.shape')
    print(dataFrame2_1.shape)
    print('dataFrame2_1.info()')
    print(dataFrame2_1.info())
    print('dataFrame2_1.Name.value_counts()')
    print(dataFrame2_1.Name.value_counts())
    print('dataFrame2_1.Name.value_counts(ascending = True)')
    print(dataFrame2_1.Name.value_counts(ascending = True))
    print('dataFrame2_1.Name.value_counts(ascending = True, dropna = True)')
    print(dataFrame2_1.Name.value_counts(ascending = True, dropna = True))
    print('dataFrame2_1.sort_values(by = [\'Name\',\'Age\'])')
    print(dataFrame2_1.sort_values(by = ['Name','Age']))

if __name__ == '__main__': main()
