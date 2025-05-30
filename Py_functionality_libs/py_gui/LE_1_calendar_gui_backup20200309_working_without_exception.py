import tkinter
from tkinter import *
from tkinter import messagebox
import calendar
import library_input_checking
import library_gui_block
from tkinter.scrolledtext import ScrolledText

# Defining the popUp size
gui_title = "Calendar"
gui_popup_size_x = "1000"
gui_popup_size_y = "500"

# Defining the text contants
input_instruction_year = "Enter year in 4 digits format, please."
input_instruction_month = "Enter month in 2 digits format, please."
incorrect_input_message = "The input is not correct. The calendar displaying is stopped"
press_buttom_text = "Press To view calendar"
name_for_button = "<Button-1>"


def get_calendar_value(event):
    calendar_text.delete(1.0, END)
    year_value = int(year_text.get())
    month_value = int(month_text.get())
    # calendar_text.insert(tkinter.END,str(calendar_value))
    calendar_exact = calendar.month(int(year_value), int(month_value))
    calendar_text.insert(tkinter.END, str(calendar_exact))
    print(calendar_exact)


print("This program displays the exact month")
input_text_left_border = 400

# PopUp2 Creating
pop_up2 = library_gui_block.main_popup(gui_title, 800, 450)
# PopUp2 lables adding
lab_month = library_gui_block.popup_label(
    pop_up2, "Defined the month number: ", label_font="Arial 12", place_x=10, place_y=10
)
lab_year = library_gui_block.popup_label(
    pop_up2, "Defined year to see: ", label_font="Arial 12", place_x=10, place_y=60
)
lab_calendar = library_gui_block.popup_label(
    pop_up2, "Calendar:: ", label_font="Arial 12", place_x=10, place_y=160
)

# PopUp2 input text for year and month adding
month_text = library_gui_block.popup_input_text(
    "month_text", pop_up2, "Arial 12", 20, 3, place_y=10, place_x=input_text_left_border
)
year_text = library_gui_block.popup_input_text(
    "year_text", pop_up2, "Arial 12", 20, 3, place_y=60, place_x=input_text_left_border
)

# output multitext box adding
calendar_text = library_gui_block.popup_input_multiline_text(
    pop_up2, 7, place_y=200, place_x=10
)

# PopUp2 button adding
see_calendar_button = library_gui_block.popup_button(
    pop_up2,
    press_buttom_text,
    name_for_button,
    get_calendar_value,
    "20",
    "Arial 12",
    place_y="120",
    place_x="10",
)

pop_up2.mainloop()

input()
