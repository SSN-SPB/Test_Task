import pandas as pd

# Read the existing Excel file
df = pd.read_excel("..\py_panda_columns_treating\py_columns_init.xlsx", engine="openpyxl")
print(df.info())  # Check data types and missing values
print(df.describe())