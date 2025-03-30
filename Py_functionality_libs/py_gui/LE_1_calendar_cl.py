import calendar
import library_input_checking

# Defining the text contants
input_instruction_year = 'Enter year in 4 digits format, please.'
input_instruction_month = 'Enter month in 2 digits format, please.'
incorrect_input_message = 'The input is not correct. The calendar displaying is stopped'

print("This program displays the exact month")
year_value = library_input_checking.define_digit_value(input_instruction_year)
month_value = library_input_checking.define_digit_value_limits(input_instruction_month, 0, 13)

calendar_exact = calendar.month(int(year_value), int(month_value))
print(calendar_exact)

input()
