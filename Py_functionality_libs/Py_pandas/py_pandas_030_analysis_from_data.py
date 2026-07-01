# Create xlsx file in python
import pandas as pd
from Py_functionality_libs.Py_pandas.py_pandas_service_methods01 import convert_data_to_excel

# Create a minimal dataset
data = {
    "name": ["Alice", None, None, "David", "David2", "David3"],
    "age": [25, -5, 30, None, 40, -35],
    "salary": [50000, 60000, None, 70000, 80000, 90000],
}


def main():
    df = pd.DataFrame(data)
    print(df)
    print(f"Dataframe head: \n{df.head()}")
    print(f"Data info: {df.info()}")
    print(f"Dataframe describe: \n{df.describe()}")
    print(f"Dataframe check null:\n{df.isnull().sum()}")
    print(f"Dataframe all null:\n{df.isnull().all}")
    print(f"Dataframe view negative age:\n{df[df['age'] < 0]}")
    # Fixing negative age values
    df.loc[df["age"] < 0, "age"] = None
    print(f"Dataframe after fixing negative age:\n{df}")
    convert_data_to_excel(df, filename="py_data_analysis.xlsx")


if __name__ == "__main__":
    main()
