#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


import pandas as pd

# read scv file to dataframe


print(pd.__version__)


def main():
    # oo = pd.read_csv('./csv_data/Olympics2.csv', skiprows=4)
    # skip rows - number of rows in csv file that should be skipped for DataFrame
    oo = pd.read_csv('./csv_data/Olympics2.csv', skiprows=4)
    # print(oo.head())
    print(oo)
    # print(oo[['City','Event']])
    print(oo.Athlete[oo.Athlete.str.contains('Jess')])
    print(oo.Event[oo.Athlete.str.contains('OWENS, Jesse')])
    print(oo[['City', 'Event', 'Edition']][oo.Athlete.str.contains('OWENS, Jesse')])
    # 
    print(oo[(oo.Medal == 'Gold') & (oo.Sport == 'Badminton') & (oo.Event == 'singles')])
    print(oo.NOC[(oo.Medal == 'Gold') & (oo.Sport == 'Badminton') & (oo.Event == 'singles')])
    # 
    NOC_selected = oo.NOC[(oo.Medal == 'Gold') & (oo.Sport == 'Badminton') & (oo.Event == 'singles')]
    print(NOC_selected.value_counts())

    # same as a single
    print((oo.NOC[(oo.Medal == 'Gold') & (oo.Sport == 'Badminton') & (oo.Event == 'singles')]).value_counts())
    #
    print(oo.NOC[(oo.Edition > 1980)])
    print(oo.NOC[(oo.Edition > 1980) & (oo.Edition < 2012)])
    print(oo[(oo.Edition > 1980) & (oo.Edition < 2012)])
    print((oo.NOC[(oo.Edition > 1976) & (oo.Edition < 2012)]).value_counts())

    # 
    NOC_selected = oo[['City', 'Event', 'NOC', 'Athlete']][
        (oo.Medal == 'Gold') & (oo.Sport == 'Badminton') & (oo.Event == 'singles')]
    print(NOC_selected.NOC.value_counts())
    print(NOC_selected.sort_values(by=['Athlete', 'NOC']))


def diff_training():
    print(type(oo))
    print('print(oo[\'City\'])')
    print(oo['City'])
    print('print(oo.City)')
    print(type(oo.City))  #
    print(oo.City)  # if no spaces in Serie
    print('print(oo[[\'City\',\'Event\']])')
    print(type(oo[['City', 'Event']]))
    print(oo[['City', 'Event']])
    print('print(oo[\'NOC\'])')
    print(type(oo['NOC']))
    print(oo['NOC'])
    print(oo.NOC)


if __name__ == '__main__': main()
