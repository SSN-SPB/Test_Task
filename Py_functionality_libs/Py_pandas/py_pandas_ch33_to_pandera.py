# pandera is a library for data validation and testing in Python.
# It provides a way to define schemas for pandas DataFrames
# and validate the data against those schemas.
# In this example, we will define a schema for a DataFrame and
# validate a dataset against it, printing both the first error
# and all errors encountered during validation.
import pandas as pd
import pandera.pandas as pa
from pandera import Column, DataFrameSchema

# Define a schema for the DataFrame
schema = DataFrameSchema({
    "name": Column(str, nullable=False),
    "age": Column(int, checks=pa.Check.in_range(0, 120), nullable=False),
    "salary": Column(float, nullable=True)
})

# Create a minimal dataset
data = {
    "name": ["Alice", None, None, "David", "David2", "David3"],
    "age": [25, -5, 30, None, 40, -35],
    "salary": [50000, 60000, None, 70000, 80000, 90000],
}


def main():
    df = pd.DataFrame(data)
    print("Dataframe first 5 values:")
    print(df.head())
    # Define and print the first error from pandera validation
    try:
        result_pandera = schema.validate(df)
        print(f"Pandera validation:\n{result_pandera}")
    except Exception as e:
        print(f"Pandera validation error:\n{e}")
    # Define and print all errors from pandera validation
    try:
        result_pandera_full = schema.validate(df, lazy=True)
        print(f"Pandera validation full:\n{result_pandera_full}")
    except Exception as e:
        print(f"Pandera validation full error:\n{e}")


if __name__ == "__main__":
    main()
