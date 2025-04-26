import pandas as pd

# Read the existing Excel file
df = pd.read_excel("py_columns_init.xlsx", engine="openpyxl")

# Add a new column (e.g., 'New Column') with some values
df["Day7"] = [
    "Value1",
    "Value2",
    "Value3",
    "Value4",
    "Value5",
    "Value6",
    "Value7",
]  # Adjust according to the length of your data

# Save the dataframe back to an Excel file
df.to_excel("py_columns_01_new_column.xlsx", index=False, engine="openpyxl")
