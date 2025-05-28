#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


# checking the difference of two column
# write to Excel
# https://www.linkedin.com/learning/pandas-essential-training/solution-2?u=2113185


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from openpyxl.workbook import Workbook

# import xlsxwriter

# plot()
# plot(kind='line')
# plot(kind='bar')
# plot(kind='barh')
# plot(kind='pie')


print(pd.__version__)


def main():
    # Plotting total number of medals in each Games

    # skiprows - number of rows in csv file that should be skipped for DataFrame
    oo = pd.read_csv("./csv_data/Olympics2.csv", skiprows=4)
    # print(oo.head())
    # print(oo)

    ## How many medals were in each game
    count_Event_medal = oo.Edition
    print(count_Event_medal)
    print(count_Event_medal.head())
    total_medal = count_Event_medal.value_counts()
    total_medal.plot(kind="bar")
    # not sorted index
    ###    plt.show()
    total_medal = count_Event_medal.value_counts().sort_index()
    total_medal.plot(kind="line")
    # sorted index
    ###    plt.show()
    # sns.countplot(x=count_Event_medal,data=count_Event_medal.value_counts(), hue='Medal')
    plt.figure(figsize=(15, 16))

    sns.countplot(x=oo.Edition, data=count_Event_medal.value_counts())
    ###    plt.show()

    ############################Challenge2#####################################
    print("############################Challenge2##########################")
    ############ Which countries did't win medat at 2008 ######################
    print("############ Which countries did't win medat at 2008 ##########")
    noc_2008 = oo[oo.Edition == 2008]
    print("print(noc_2008)")
    print(noc_2008)
    ###    sns.countplot(x=oo.NOC,data= noc_2008.value_counts())
    ###    plt.show()

    ### print OlympicNOC
    olimpicNOC = pd.read_csv("IOC_COUNTRY_CODES.csv")
    print("(olimpicNOC)")
    print(olimpicNOC)
    ### Response
    #             Country Int Olympic Committee code ISO code        Country.1
    # 0        Afghanistan                        AFG       AF      Afghanistan
    # 1            Albania                        ALB       AL          Albania

    ### Check the diffrence of two columns
    nc_dif = olimpicNOC[olimpicNOC["Country"] != olimpicNOC["Country.1"]]
    print("Country vs Country.1 diff")
    print(nc_dif.head())

    ### check the existing diff in two columns
    ### print OlympicNOC
    olimpicNOC_ed = pd.read_csv("IOC_COUNTRY_CODES_ed.csv")
    nc_dif2 = olimpicNOC_ed[olimpicNOC_ed["Country"] != olimpicNOC_ed["Country.1"]]
    print("Country vs Country.1 existing diff")
    print(nc_dif2.head())

    ### Setting index by noc
    # reseting the index
    olimpicNOC.set_index("Int Olympic Committee code", inplace=True)
    print("(olimpicNOC with index {}".format("Int Olympic Committee code"))
    print(olimpicNOC)
    ### define NOC that won medals in 2008
    medal_2008 = noc_2008.NOC.value_counts()
    print("define NOC that won medals in 2008")
    print(medal_2008)
    ### final result - define NOC that didn' win medals in 2008
    olimpicNOC["medal_2008"] = medal_2008
    fr = olimpicNOC.medal_2008  # .isnull()
    print("print combined list")
    print(olimpicNOC)
    print("print value Null notNUll is 2008 for each NOC")
    print(fr)
    fr = olimpicNOC[olimpicNOC.medal_2008.isnull()]
    print("print Null medal list_combined list")
    print(fr)
    print("fr.to_excel output2.xlsx  Null value is not added to excel")
    # fr.to_excel("output.xlsx", engine='xlsxwriter')
    fr.to_excel("output2.xlsx")


if __name__ == "__main__":
    main()
