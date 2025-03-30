#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov

# plotting colors
# Sequential - representing information that has ordering
## Change in lightness (over a single hue)
# Greens, Blues, Reds
# Diverging - color is deviate round a middle value
# RdGy, bwr, Spectral
# Qualitative - infromation that has not an ordering or relationship
# Pastel1, Pastel2, tab10, tab20, ..
# pattern
# https://matplotlib.org/_images/colormaps_reference_02.png
# https://matplotlib.org/_images/colormaps_reference_03.png

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# plot()
# plot(kind='line')
# plot(kind='bar')
# plot(kind='barh')
# plot(kind='pie')


print(pd.__version__)

def main():
    # skiprows - number of rows in csv file that should be skipped for DataFrame
    oo = pd.read_csv('./csv_data/Olympics2.csv', skiprows=4)
    # print(oo.head())
    print(oo)
    ## Chinese team in Beijing 2008
    count_Chinese_medal= oo.Medal[(oo.NOC == 'CHN') & (oo.City == 'Beijing')]
    print(count_Chinese_medal)
    print(count_Chinese_medal.head())

    count_Chinese_all_medal= oo[(oo.NOC == 'CHN') & (oo.City == 'Beijing')]
    print(count_Chinese_all_medal)
    print(count_Chinese_all_medal.head())
    print('print(count_Chinese_all_medal.Gender.value_counts())')
    print(count_Chinese_all_medal.Gender.value_counts())
    current_pd=count_Chinese_all_medal.Gender.value_counts()
    current_pd.plot (kind = 'bar')
    plt.show()
    sns.countplot(x=count_Chinese_all_medal.Gender,data=count_Chinese_all_medal)
    plt.show()
    sns.countplot(x=count_Chinese_all_medal.Medal,data=count_Chinese_all_medal)
    plt.show()

# hue 
    sns.countplot(x=count_Chinese_all_medal.Medal,data=count_Chinese_all_medal, hue=count_Chinese_all_medal.Gender)
    plt.show()
# hue 
    sns.countplot(x=count_Chinese_all_medal.Medal,data=count_Chinese_all_medal, hue=count_Chinese_all_medal.Gender, order =['Bronze', 'Silver', 'Gold'])
    plt.show()
# hue 
    sns.countplot(x='Gender',data=count_Chinese_all_medal, hue='Medal')
    plt.show()
# palette
    sns.countplot(x='Gender',data=count_Chinese_all_medal, palette='bwr')
    plt.show()
# hue and palette
    sns.countplot(x='Gender',data=count_Chinese_all_medal,
                  hue='Medal', palette='cool')
    plt.show()
# palette and hue_order
    sns.countplot(x='Gender',data=count_Chinese_all_medal,
                  hue='Medal', hue_order =['Bronze', 'Silver', 'Gold'])
    plt.show()

# hue and order
    sns.countplot(x='Medal',data=count_Chinese_all_medal,
                  hue='Gender',order =['Bronze', 'Silver', 'Gold'])
    plt.show()
    
        
def diff_training():
    print(type(oo))
    print('print(oo[\'City\'])')
    print(oo['City'])
    print('print(oo.City)')
    print(type(oo.City)) # 
    print(oo.City) # if no spaces in Serie
    print('print(oo[[\'City\',\'Event\']])')
    print(type(oo[['City','Event']]))
    print(oo[['City','Event']])
    print('print(oo[\'NOC\'])')
    print(type(oo['NOC']))
    print(oo['NOC'])
    print(oo.NOC)
    
if __name__ == '__main__': main()
