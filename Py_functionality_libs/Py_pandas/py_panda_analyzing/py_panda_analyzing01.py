import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read the existing Excel file
df = pd.read_excel("..\py_panda_columns_treating\py_columns_init.xlsx", engine="openpyxl")
print(df.info())  # Check data types and missing values
print(df.describe())

# missing_data = df.isnull().sum()
# print(f'Missing data per column:\n{missing_data}')
#
# # Visualize missing data with a heatmap
# sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
# plt.title('Missing Data Visualization')
# plt.show()
#
# plt.scatter(df['Day1'], df['Day3'])
# plt.title('Scatter plot of column1 vs column2')
# plt.show()
empty_cells = df.isna()

# Loop to show addresses
for row_idx, col_name in zip(*empty_cells.to_numpy().nonzero()):
    print(f"Empty cell at Row {row_idx}, Column '{df.columns[col_name]}'")

print(df['Day1'])