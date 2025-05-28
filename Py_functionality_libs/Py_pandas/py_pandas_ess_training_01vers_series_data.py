#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


import pandas as pd

# pandas version
# pandas Series creating
# pandas DataFrame creating


def main():
    print(pd.__version__)
    # pd.show_versions()
    series_index = list(range(2, 10, 2))
    print(series_index)
    age = [21, 41, 61, 81]
    first_name = ["John", "Bill", "Ronald", "Jimm"]
    state = ["CO", "AR", "NY", "CA"]
    columns_data = ["Age", "Name", "State"]
    serie1 = pd.Series(age, index=series_index)
    serie2 = pd.Series(first_name, index=series_index)
    serie3 = pd.Series(state, index=series_index)
    print(serie3)
    data_frame1 = {"A": age, "B": first_name, "C": state}
    print("data_frame1")
    print(data_frame1)

    dataFrame1 = pd.DataFrame(data_frame1, index=series_index)
    print("dataFrame1")
    print(dataFrame1)
    print(dataFrame1.B)
    # row data
    data_frame2 = (age, first_name, state)
    print(data_frame2)
    dataFrame2 = pd.DataFrame(data_frame2)
    print(dataFrame2)
    # transponse row data
    dataFrame2_1 = dataFrame2.transpose()
    print("dataFrame2_1")
    print(dataFrame2_1)
    # adding columns
    dataFrame2_1.columns = columns_data
    # addint indexes
    dataFrame2_1.index = series_index
    print(dataFrame2_1)


if __name__ == "__main__":
    main()
