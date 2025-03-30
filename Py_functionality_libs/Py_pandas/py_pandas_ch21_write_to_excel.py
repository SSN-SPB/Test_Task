#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


# checking the difference of two column
# write to Excel
# https://www.linkedin.com/learning/pandas-essential-training/solution-2?u=2113185


import pandas as pd
# import xlsxwriter

# plot()
# plot(kind='line')
# plot(kind='bar')
# plot(kind='barh')
# plot(kind='pie')


def main():

    
    # skiprows - number of rows in csv file that should be skipped for DataFrame
    oo = pd.read_csv('./csv_data/Olympics2.csv', skiprows=4)
    # print(oo.head())
    # print(oo)



############################Challenge2#####################################
    print('############################Challenge2##########################')    
############ Which countries did't win medat at 2008 ######################
    print('############ Which countries did\'t win medals at 2008 ##########')
    noc_2008 = oo[oo.Edition == 2008]
    print('print(noc_2008)')
    print(noc_2008)
###    sns.countplot(x=oo.NOC,data= noc_2008.value_counts())
###    plt.show()

### print OlympicNOC
    olympicNOC = pd.read_csv('IOC_COUNTRY_CODES.csv')
    print('(olimpicNOC)')
    print(olympicNOC)
### Response
#             Country Int Olympic Committee code ISO code        Country.1
#0        Afghanistan                        AFG       AF      Afghanistan
#1            Albania                        ALB       AL          Albania


### Check the diffrence of two columns
    nc_dif = olympicNOC [olympicNOC['Country'] != olympicNOC['Country.1']]
    print('Country vs Country.1 diff')
    print(nc_dif.head())

### check the existing diff in two columns
    ### print OlympicNOC
    olympicNOC_ed = pd.read_csv('IOC_COUNTRY_CODES_ed.csv')
    nc_dif2 = olympicNOC_ed [olympicNOC_ed['Country'] != olympicNOC_ed['Country.1']]
    print ('Country vs Country.1 existing diff')
    print(nc_dif2.head())

### Setting index by noc
    #reseting the index
    olympicNOC.set_index('Int Olympic Committee code', inplace=True)
    print('(olimpicNOC with index {}'.format('Int Olympic Committee code'))
    print(olympicNOC)
### define NOC that won medals in 2008
    medal_2008 = noc_2008.NOC.value_counts()
    print('define NOC that won medals in 2008')
    print(medal_2008)
### final result - define NOC that didn' win medals in 2008
    olympicNOC['medal_2008'] = medal_2008
    fr=olympicNOC.medal_2008  # .isnull()
    print('print combined list')
    print(olympicNOC)
    print('print value Null notNUll is 2008 for each NOC')
    print(fr)
    fr=olympicNOC[olympicNOC.medal_2008.isnull()]
    print('print Null medal list_combined list')
    print(fr)
    print('fr.to_excel output2.xlsx REMARK: medal_2008 values are not added to excel')
    ############################################################
    #! medal_2008 values are not added to excel - inverstigate
    #fr.to_excel("output.xlsx", engine='xlsxwriter')  
    fr.to_excel('output2.xlsx')
    with pd.ExcelWriter('output_combined.xlsx') as writer:
        fr.to_excel(writer, sheet_name='SelectecNOC')
        noc_2008.to_excel(writer, sheet_name='NOC_winners2008_1')



    
if __name__ == '__main__': main()
