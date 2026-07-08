import xlsxwriter
# pip install XlsxWriter
# xlsxwriter is a Python module for creating Excel XLSX files.
# It can be used to write text, numbers, formulas,
# and hyperlinks to multiple worksheets in an Excel 2007+ XLSX file.
# It supports features such as formatting and many more, including charts.


def add_data_to_excel(x):
    def inner_function(y):
        return x * y

    return inner_function


def main():
    workbook = xlsxwriter.Workbook("test.xlsx")
    worksheet = workbook.add_worksheet()

    worksheet.set_column("A:A", 21)
    worksheet.set_column("B:D", 31)
    worksheet.write("A1", "Hello World27lul08x`")
    worksheet.insert_image("B1", "test_image.png")
    workbook.close()


if __name__ == "__main__":
    main()
