import os


def convert_data_to_excel(df, filename="py_data.xlsx"):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print("File not found. May proceed with creating new file.")
        pass
    df.to_excel(filename, index=False, engine="openpyxl")
    if os.path.exists(filename):
        print("excel file created successfully")
    else:
        print("excel file creation failed")
