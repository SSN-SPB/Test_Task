#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


from pandas import DataFrame
import matplotlib.pyplot as plt


def main():
    Data = {'Unemployment_Rate': [6.1,5.8,5.7,5.7,5.8,5.6,5.5,5.3,5.2,5.2],
        'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
       }
  
    df = DataFrame(Data,columns=['Unemployment_Rate','Stock_Index_Price'])
    # df.plot(x ='Unemployment_Rate', y='Stock_Index_Price', kind = 'scatter')
    df.plot(x ='Unemployment_Rate', y='Stock_Index_Price', kind = 'bar')
    plt.show()          
if __name__ == '__main__': main()
