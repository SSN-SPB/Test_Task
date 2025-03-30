#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


import pandas as pd
# pandas info
# pandas tail
# pandas head



def main():
    series_index = list(range(2,12,2))
    age = [21, 41, 61, 81, None]
    first_name = ['John', 'Bill', 'Ronald', 'Jimm','Jordge']
    state = ['CO', 'AR', 'NY', 'CA', None]
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
    print('dataFrame2_1.head(2)')
    print(dataFrame2_1.head(2))
    print('dataFrame2_1.tail(2)')
    print(dataFrame2_1.tail(2))    


if __name__ == '__main__': main()
