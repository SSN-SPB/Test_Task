#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov

# indexing
# https://www.linkedin.com/learning/pandas-essential-training/index?u=2113185

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
    #print(list(oo.index))
    print(oo.index[100])
    try:
        oo.index[100] = 3
    except TypeError:
        print ('Input is not allowed')
        print ('found error: {}'.format(sys.exc_info()[1]))
    #set temporaty index
    oo.set_index('Sport')
    print('oo.set_index(Sports)')
    print(oo.head())
    foo_sport = oo.set_index('Sport')
    print('foo_sport = oo.set_index(Sport)')
    print(foo_sport.head())
    #set saved index
    oo.set_index('Sport', inplace=True)
    print('oo.set_index(Sports), inplace=True')
    print(oo.head())
    #reseting the index
    oo.reset_index( inplace=True)
    print('oo.reset_index( inplace=True)')
    print(oo.head())
    #plotting the changed index
    print('plotting the changed index - df = foo_sport.Medal.value_counts()')
    df = foo_sport.Medal.value_counts()
    print(df)
    df.plot(x=df.index, y=oo.Medal.value_counts(),kind = 'pie')
    plt.show()
    df.plot(x=df.index, y=df,kind = 'bar')
    plt.show()    



    
if __name__ == '__main__': main()
