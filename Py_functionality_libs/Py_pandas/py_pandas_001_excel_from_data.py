# Create xlsx file in python
import pandas as pd
import os

# Create a minimal dataset
data = {
    "featureOne": [1.0, 2.0, 3.0, 4.5, 5.0, 3.5, 2.2, 1.5, 3.0, 4.0],
    "featureTwo": [2.0, 1.0, 4.0, 3.2, 2.5, 3.5, 4.1, 2.2, 3.0, 2.0],
    "featureThree": [3.0, 3.5, 2.0, 1.0, 4.0, 3.5, 2.2, 1.8, 3.0, 1.5],
    "labels": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
}


def main():
    df = pd.DataFrame(data)
    try:
        os.remove("py_columns_init.xlsx")
    except FileNotFoundError:
        print("File not found. May proceed with creating new file.")
        pass
    df.to_excel("py_columns_init.xlsx", index=False, engine="openpyxl")
    if os.path.exists("py_columns_init.xlsx"):
        print("excel file created successfully")
    else:
        print("excel file creation failed")


if __name__ == "__main__":
    main()
