#!/usr/bin/env python3
# The 1s line is ignored in Win

import tkinter
from tkinter import *
from tkinter import messagebox
import calendar
import library_input_checking
import library_gui_block
from tkinter.scrolledtext import ScrolledText

# Genearal constant
num_7 = "7"
num_10 = "10"
num_20 = "20"

# Defining the popUp size and contstants
gui_title = "Calendar"
gui_popup_size_x = "800"
gui_popup_size_y = "600"
input_text_left_border = "300"
font_Arial_12 = "Arial 12"
# listbox constants
lb_height_sel = 4
lb_width_sel = 300

# Defining the text constants
input_instruction_year = "Enter year in 4 digits format, please."
input_instruction_month = "Enter month in 2 digits format, please."
incorrect_input_message = (
    "The input is not correct." " The calendar displaying is stopped"
)
press_button_text = "Press To view calendar"
name_for_button = "<Button-1>"
wrong_value_message = "Some input data is wrong." " Check it and try to reenter, please"
select_month_text = "Select the month number: "
wrong_text_message = "wrong_text_message"
text_calendar = "Calendar: "
text_service_info = "Service info: "
text_define_year = "Defined year to see: "
text_year = "year_text"


def get_calendar_value(event):
    calendar_text.delete(1.0, END)
    wrong_input_text.delete(0, END)

    # Check if the input data is correct and result
    # is calculated successfully
    try:
        # get year value from year text
        year_value = int(year_text.get())
        # get value from cursor selection
        cursor_selection_value = list_input.curselection()
        # get value from list
        month_value = int(list_input.get(cursor_selection_value))
        # month_value=int(month_text.get())
        calendar_exact = calendar.month(int(year_value), int(month_value))
    except:
        print(wrong_value_message)
        # calendar_text.insert(tkinter.END,wrong_value_message)
        wrong_input_text.insert(tkinter.END, wrong_value_message)

    calendar_text.insert(tkinter.END, str(calendar_exact))
    print(calendar_exact)


print("This program displays the exact month")

# Placement constants
first_row_y = 10
step_row = 50

# PopUp2 Creating
pop_up2 = library_gui_block.main_popup(gui_title, gui_popup_size_x, gui_popup_size_y)
# PopUp2 labels adding
lab_year = library_gui_block.popup_label(
    pop_up2,
    text_define_year,
    label_font=font_Arial_12,
    place_x=num_10,
    place_y=first_row_y + step_row * 2,
)
lab_calendar = library_gui_block.popup_label(
    pop_up2,
    text_calendar,
    label_font=font_Arial_12,
    place_x=num_10,
    place_y=first_row_y + step_row * 5,
)
lab_service = library_gui_block.popup_label(
    pop_up2,
    text_service_info,
    label_font=font_Arial_12,
    place_x=num_10,
    place_y=first_row_y + step_row * 9,
)
lab_month_list = library_gui_block.popup_label(
    pop_up2,
    select_month_text,
    label_font=font_Arial_12,
    place_x=num_10,
    place_y=first_row_y + step_row * 0,
)

# PopUp2 input text for year and month adding
row_num = 2
y_place = first_row_y + step_row * row_num
year_text = library_gui_block.popup_input_text(
    text_year,
    pop_up2,
    font_Arial_12,
    20,
    3,
    place_y=y_place,
    place_x=input_text_left_border,
)
row_num = 10
y_place = first_row_y + step_row * row_num
wrong_input_text = library_gui_block.popup_input_text(
    wrong_text_message, pop_up2, font_Arial_12, 60, 3, place_y=y_place, place_x=num_10
)
# months_list_creating
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
x_place = input_text_left_border
row_num = 0
y_place = first_row_y + step_row * row_num
list_input = library_gui_block.popup_input_text_list(
    pop_up2,
    months,
    place_x=x_place,
    place_y=y_place,
    listbox_height=lb_height_sel,
    listbox_width=lb_width_sel,
)
# output multitext box adding
row_num = 6
y_place = first_row_y + step_row * row_num
calendar_text = library_gui_block.popup_input_multiline_text(
    pop_up2, num_7, place_y=y_place, width_of_multitext=60, place_x=num_10
)

# PopUp2 button adding
row_num = 4
y_place = first_row_y + step_row * row_num
see_calendar_button = library_gui_block.popup_button(
    pop_up2,
    press_button_text,
    name_for_button,
    get_calendar_value,
    num_20,
    font_Arial_12,
    place_y=y_place,
    place_x=num_10,
)

pop_up2.mainloop()

input()
