import tkinter
from tkinter import *
from tkinter import messagebox

print("This program converts the temperature from Fahrenheit to Celsius")
instrustion_input = 'Input your temperature in Fahrenheit '
press_buttom_text = 'Press to convert'
you_result_label = 'The temperature in Celsius'
wrong_value_message = 'The entered value is not the digit. Try one more time please.'
gui_title = 'Fahrenheit to Celsius'
gui_size_x = '700'
gui_size_y = '250'


# Create main function that calculates Celsius temperature
def convert_fahrenheit_to_celsius(event):
    # Clean tkinter GUI forms
    out_text.delete(0, 20)
    output_message.delete(0, 120)
    # Get in_text.get() value is taken from form
    try:
        temperatureInFahrenheit = int(in_text.get())
    except:
        print(wrong_value_message)
        # Output GUI message log for invalid input
        output_message.insert(tkinter.END, wrong_value_message)

    temperatureInCelsius = int(temperatureInFahrenheit - 32) / 1.8
    # Displaying the final value in GUI form
    out_text.insert(tkinter.END, int(temperatureInCelsius))
    # Output GUI message for good scenario
    output_message.insert(tkinter.END, 'The temperature in Celsius is: %d degrees' % temperatureInCelsius)

    print('The temperature in Celsius is: %d degrees' % temperatureInCelsius)


# Creating main GUI popUp
root = tkinter.Tk()
root.title(gui_title)
root_reomentry = gui_size_x + 'x' + gui_size_y
root.geometry(root_reomentry)

# Creating vidgets within popUp
in_text = tkinter.Entry(root, width=20, bd=3, font='Arial 12')
lab1 = tkinter.Label(root, text=instrustion_input, font='Arial 12')
lab2 = tkinter.Label(root, text=you_result_label, font='Arial 12')
but1 = tkinter.Button(root, text=press_buttom_text, width=20,
                      font='Arial 12')
out_text = tkinter.Entry(root, width=20, bd=3, font='Arial 12')
# web source for messaging https://www.tutorialspoint.com/python/tk_message.htm
output_message = tkinter.Entry(root, width=60, text=you_result_label, font='Arial 12')

# Placing vidgets into popUp
left_border_for_figures = 400
in_text.place(x=left_border_for_figures, y=10)
out_text.place(x=left_border_for_figures, y=100)
but1.place(x=10, y=50)
lab1.place(x=10, y=10)
lab2.place(x=10, y=100)
output_message.place(x=10, y=150)

# Connect function and clicking the Button1
but1.bind('<Button-1>', convert_fahrenheit_to_celsius)

root.mainloop()
