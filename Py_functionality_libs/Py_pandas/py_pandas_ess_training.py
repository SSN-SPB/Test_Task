#!/usr/bin/env python3
# Copyright 2020 Sergei Smirnov


import pandas as pd

# pandas version
# pandas Series creating
# pandas DataFrame creating


print(pd.__version__)


def main():
    print(pd.__version__)
    series_index = list(range(2, 10, 2))
    print(series_index)
    results = [21, 41, 61, 81]
    results2 = [211, 411, 611, 811]
    results3 = ["a211", "a411", "a611", "a811"]
    columns_data = ["A", "B", "C"]
    serie1 = pd.Series(results, index=series_index)
    serie2 = pd.Series(results2, index=series_index)
    serie3 = pd.Series(results3, index=series_index)
    print(serie3)
    # pd.show_versions()
    # dataFrame1=pd.DataFrame[serie1, serie2, serie3]
    data_frame1 = {"A": results, "B": results2, "C": results2}
    dataFrame1 = pd.DataFrame(data_frame1, index=series_index)
    print(dataFrame1)
    print(dataFrame1.B)


if __name__ == "__main__":
    main()
