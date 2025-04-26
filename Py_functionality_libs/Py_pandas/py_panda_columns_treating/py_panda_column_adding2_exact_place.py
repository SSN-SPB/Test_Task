import pandas as pd

# Read the existing Excel file
df = pd.read_excel("py_columns_init.xlsx", engine="openpyxl")

# Add a new column (e.g., 'New Column') with some values
inserted_values = [
    "Value1",
    "Value2",
    "Value3",
    "Value4",
    "Value5",
    "Value6",
    "Value7",
]  # Adjust according to the length of your data

# Get the index of 'ColumnB'
insert_at = df.columns.get_loc("Day3")

# Step 4: Insert the new column before Day3 column
df.insert(insert_at, "Day7", inserted_values)


# Save the dataframe back to an Excel file
df.to_excel("py_columns_02_new_column_exact_place.xlsx", index=False, engine="openpyxl")
