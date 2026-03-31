# Create xlsx file in python
import pandas as pd
from great_expectations.dataset import PandasDataset

# Create a minimal dataset
data = {
    "name": ["Alice", None, None, "David", "David2", "David3"],
    "age": [25, -5, 30, None, 40, -35],
    "salary": [50000, 60000, None, 70000, 80000, 90000],
}


def main():
    df = pd.DataFrame(data)
    print("Dataframe describe:")
    print(df.describe())
    print(df)
    df_ge = PandasDataset(df)

    result_name = df_ge.expect_column_values_to_not_be_null("name")
    result_age = df_ge.expect_column_values_to_be_between("age", min_value=-75, max_value=120)
    print(f"GE name:\n{result_name}")
    print(f"GE age:\n{result_age}")

if __name__ == "__main__":
    main()
