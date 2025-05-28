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

# %matplotlib inline

# plot()
# plot(kind='line')
# plot(kind='bar')
# plot(kind='barh')
# plot(kind='pie')

import numpy as np

x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()


print(pd.__version__)


def main():
    # oo = pd.read_csv('./csv_data/Olympics2.csv', skiprows=4)
    # skiprows - number of rows in csv file that should be skipped for DataFrame
    oo = pd.read_csv("./csv_data/Olympics2.csv", skiprows=4)
    # print(oo.head())
    print(oo)
    fo = oo[oo.Edition == 1896]
    print(fo.head())
    print(fo.Sport.value_counts())
    # print(fo.Sport.value_counts().plot(kind='bar'))

    df = fo.Sport.value_counts()
    print(df)
    # df.plot(x=fo.Sport, y=fo.Sport.value_counts(), kind = 'line')
    # df.plot(x=fo.Sport, y=fo.Sport.value_counts(), kind = 'pie')
    # specify color
    df.plot(x=fo.Sport, y=fo.Sport.value_counts(), kind="line", color="maroon")
    plt.show()

    # df.plot(x=fo.Sport, y=fo.Sport.value_counts(), figsize=(15,2),kind = 'line', color='maroon')
    # plt.show()
    df.plot(x=fo.Sport, y=fo.Sport.value_counts(), figsize=(10, 4), kind="pie")
    plt.show()
    df.plot(
        x=fo.Sport,
        y=fo.Sport.value_counts(),
        figsize=(10, 4),
        kind="pie",
        colormap="Pastel1",
    )
    plt.show()
    df.plot(
        x=fo.Sport,
        y=fo.Sport.value_counts(),
        figsize=(10, 4),
        kind="pie",
        colormap="Pastel2",
    )
    plt.show()
    df.plot(
        x=fo.Sport,
        y=fo.Sport.value_counts(),
        figsize=(10, 4),
        kind="pie",
        colormap="tab10",
    )
    plt.show()
    df.plot(
        x=fo.Sport,
        y=fo.Sport.value_counts(),
        figsize=(10, 4),
        kind="pie",
        colormap="bwr",
    )
    plt.show()
    df.plot(
        x=fo.Sport,
        y=fo.Sport.value_counts(),
        figsize=(10, 4),
        kind="pie",
        colormap="Greens",
    )
    plt.show()

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
