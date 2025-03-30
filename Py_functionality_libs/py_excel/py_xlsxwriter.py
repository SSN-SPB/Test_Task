import xlsxwriter




def add_data_to_excel(x):
    def inner_function(y):
        return x * y
    return inner_function


def main():
    workbook = xlsxwriter.Workbook('test.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:D', 30)
    worksheet.write('A1', 'Hello World2')
    worksheet.insert_image('B1', 'test_image.png')
    workbook.close()


if __name__ == "__main__":
    main()
