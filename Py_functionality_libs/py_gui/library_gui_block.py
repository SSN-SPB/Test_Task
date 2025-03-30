import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

# Contant names:
font_Arial_12 = 'Arial 12'


# Create main function that calculates Celsius temperature
def main_popup(title, gui_size_x, gui_size_y):
    root = tkinter.Tk()
    root.title(title)
    root_reomentry = str(gui_size_x) + 'x' + str(gui_size_y)
    root.geometry(root_reomentry)
    return root


def popup_label(root, label_text, label_font=font_Arial_12,
                place_x=10,
                place_y=10):
    lab = tkinter.Label(root, text=label_text, font=label_font)
    lab.place(x=place_x, y=place_y)


def popup_input_text(textname, popup_name,
                     label_font=font_Arial_12,
                     text_width=20,
                     text_bd=3,
                     place_x=10,
                     place_y=200):
    textname = tkinter.Entry(popup_name,
                             width=text_width,
                             bd=3,
                             font=label_font)
    textname.place(x=place_x, y=place_y)
    return textname


# https://younglinux.info/tkinter/widget2.php
# https://metanit.com/python/tutorial/9.9.php
def popup_input_text_list(root, list_content, place_x, place_y,
                          listbox_height, listbox_width):
    target_list = Listbox(height=listbox_height)
    for i in list_content:
        target_list.insert(END, i)
    target_list.place(x=place_x, y=place_y, width=listbox_width)
    ## scroll bar to main frame by default
    scrollbar_listbox = Scrollbar(target_list, command=target_list.yview)
    scrollbar_listbox.pack(side=RIGHT, fill=Y)
    # https://stackoverflow.com/questions/13832720/how-to-attach-a-scrollbar-to-a-text-widget/13833338

    # attach listbox to scrollbar
    target_list.config(yscrollcommand=scrollbar_listbox.set)
    return target_list

    textname_list = tkinter.Entry(popup_name, width=text_width,
                                  bd=3, font=label_font)
    textname.place(x=place_x, y=place_y)
    return textname_list


def popup_input_multiline_text(root, height_input, place_x=10,
                               place_y=100, width_of_multitext=30):
    input_multiline_text = ScrolledText(root, height=height_input,
                                        width=width_of_multitext);
    input_multiline_text.place(x=place_x, y=place_y)
    return input_multiline_text


def popup_input_multiline_text_grid(root, height_input, row_input, column_input):
    input_multiline_text = ScrolledText(root, height=height_input);
    input_multiline_text.grid(row=row_input, column=column_input)
    return input_multiline_text


def popup_label_grid(root, label_text, row_number, justify_lab):
    lab = tkinter.Label(root, text=label_text,
                        justify=justify_lab).grid(row=row_number)


def popup_input_text_grid(popup_name, row_number, column_number):
    input_text_field_grid = tkinter.Entry(popup_name).grid(row=row_number, column=column_number)
    return input_text_field_grid


def popup_button(popup_name, press_buttom_text, button_name,
                 function_name, button_width=20,
                 button_font=font_Arial_12, place_x='10',
                 place_y='10'):
    but = tkinter.Button(popup_name,
                         text=press_buttom_text,
                         width=button_width,
                         font=button_font)
    but.bind(button_name, function_name)
    but.place(x=place_x, y=place_y)
    return but
