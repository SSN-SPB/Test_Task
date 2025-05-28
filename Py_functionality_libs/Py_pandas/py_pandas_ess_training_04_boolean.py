#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


import pandas as pd

# pandas boolean
# https://www.linkedin.com/learning/pandas-essential-training/boolean-indexing?u=2113185


def main():
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
    print("dataFrame2_1.shape")
    print(dataFrame2_1.shape)
    print("dataFrame2_1.info()")
    print(dataFrame2_1.info())

    print("dataFrame2_1[dataFrame2_1.Name == 'Jimm']")
    print(dataFrame2_1[dataFrame2_1.Name == "Jimm"])
    print("dataFrame2_1[(dataFrame2_1.Name == 'Jimm') & (dataFrame2_1.Age < 71)]")
    print(dataFrame2_1[(dataFrame2_1.Name == "Jimm") & (dataFrame2_1.Age < 71)])


if __name__ == "__main__":
    main()
