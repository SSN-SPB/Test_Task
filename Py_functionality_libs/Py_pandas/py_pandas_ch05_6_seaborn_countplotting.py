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
    oo = pd.read_csv("./csv_data/Olympics2.csv", skiprows=4)
    # print(oo.head())
    print(oo)
    fo = oo[oo.Edition == 1896]
    print(fo.head())
    print(fo.Sport.value_counts())
    df = fo.Sport.value_counts()
    print(df)
    # df.plot(x=fo.Sport, y=fo.Sport.value_counts(), kind = 'line')
    # df.plot(x=fo.Sport, y=fo.Sport.value_counts(), kind = 'pie')
    # specify color
    df.plot(x=fo.Sport, y=fo.Sport.value_counts(), kind="line", color="maroon")
    plt.show()

    df.plot(
        x=fo.Sport,
        y=fo.Sport.value_counts(),
        figsize=(10, 4),
        kind="pie",
        colormap="Greens",
    )
    plt.show()
    df.plot(
        x=fo.Sport,
        y=fo.Sport.value_counts(),
        figsize=(10, 4),
        kind="line",
        colormap="Greens",
    )
    plt.show()
    print("countplot")
    sns.countplot(x="Medal", data=oo)
    x = sns.countplot(x="Medal", data=oo)
    plt.show()
    # change seeborn size
    sns.set(rc={"figure.figsize": (20, 4)})
    sns.countplot(x="City", data=oo)
    # plt.subplots(figsize=(10,4))

    plt.show()
    print("countplot completed")

    # second Db

    series_index = list(range(2, 16, 2))
    age = [21, 41, 61, 71, None, 61, 38]
    first_name = ["John", "Bill", "Jimm", "Jimm", "Jordge", "Jimm", "Jimm"]
    state = ["CO", "AR", "NY", "CA", None, "AR", "MA"]
    columns_data = ["Age", "Name", "State"]

    # row data
    data_frame2 = (age, first_name, state)
    dataFrame2 = pd.DataFrame(data_frame2)
    # transponse row data
    dataFrame2_1 = dataFrame2.transpose()
    # adding columns
    dataFrame2_1.columns = columns_data
    # addint indexes
    dataFrame2_1.index = series_index
    print(dataFrame2_1)
    # dataFrame2_1.plot(x = series_index, y=dataFrame2_1.Age, kind = 'bar')


def diff_training():
    print(type(oo))
    print("print(oo['City'])")
    print(oo["City"])
    print("print(oo.City)")
    print(type(oo.City))  #
    print(oo.City)  # if no spaces in Serie
    print("print(oo[['City','Event']])")
    print(type(oo[["City", "Event"]]))
    print(oo[["City", "Event"]])
    print("print(oo['NOC'])")
    print(type(oo["NOC"]))
    print(oo["NOC"])
    print(oo.NOC)


if __name__ == "__main__":
    main()
