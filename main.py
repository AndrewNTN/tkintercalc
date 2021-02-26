import tkinter
from tkinter import RIGHT, END, DISABLED, NORMAL
import re

# Define colors and fonts
bg = "#768e72"
green = "#7fa580"
cream = "#eee2d0"
button_font = ("Arial Black", 18)
display_font = ("Arial Black", 30)

# Define window
root = tkinter.Tk()
root.title("Calculator")
root.geometry('330x440')
root.resizable(0, 0)
root.config(bg=bg)


# Define functions
def clear():
    display.config(state=NORMAL)
    display.delete(first=0, last=END)
    enable_buttons()


# deletes rightmost character
def delete():
    display.delete(first=len(display.get())-1, last=END)


def submit_number(number):
    display.insert(END, number)


def equal():
    try:
        solution = eval(display.get())
        display.delete(first=0, last=END)
        display.insert(0, solution)
    # if equation is invalid returns syntax error
    except SyntaxError:
        display.delete(first=0, last=END)
        display.insert(0, "Syntax Error  ")
        # makes only AC and QUIT buttons available
        for bt in bt_list:
            bt.config(state=DISABLED)
        display.config(state=DISABLED)
        quit_button.config(state=NORMAL)
        clear_button.config(state=NORMAL)


def negate():
    # searches for the rightmost number
    pattern = "\d+?\.?\d{0,}$"
    m = re.search(pattern, display.get())
    # surrounds rightmost number with -()
    display.insert(m.span()[1], ")")
    display.insert(m.span()[0], "-(")


def inverse():
    display.insert(0, "1/(")
    display.insert(END, ")")


def enable_buttons():
    for bt in bt_list:
        bt.config(state=NORMAL)


# GUI Layout
# Define frames
display_frame = tkinter.LabelFrame(root, bd=0, bg=bg)
button_frame = tkinter.LabelFrame(root, bd=0, bg=bg)
display_frame.pack(padx=2, pady=(5, 20))
button_frame.pack(padx=2, pady=5)

# Layout for the display frame
display = tkinter.Entry(display_frame, width=50, font=display_font, bg=cream, fg=green, borderwidth=0, justify=RIGHT,
                        insertbackground=green)
display.pack(padx=5, pady=5)

# Layout for the button frame
clear_button = tkinter.Button(button_frame, text="AC", font=button_font, bg=green, fg=cream, bd=0, activeforeground=bg,
                              command=clear)
quit_button = tkinter.Button(button_frame, text="Quit", font=button_font, bg=green, fg=cream, bd=0, activeforeground=bg,
                             command=root.destroy)

inverse_button = tkinter.Button(button_frame, text='1/x', font=button_font, fg=green, bg=cream, bd=0,
                                activeforeground=bg, command=inverse)
square_button = tkinter.Button(button_frame, text='x^2', font=button_font, fg=green, bg=cream, bd=0,
                               activeforeground=bg, command=lambda: submit_number("**2"))
exponent_button = tkinter.Button(button_frame, text='x^n', font=button_font, fg=green, bg=cream, bd=0,
                                 activeforeground=bg, command=lambda: submit_number("**"))
delete_button = tkinter.Button(button_frame, text='del', font=button_font, bg=green, fg=cream, bd=0,
                               activeforeground=bg, command=delete)
divide_button = tkinter.Button(button_frame, text=' / ', font=button_font, fg=green, bg=cream, bd=0,
                               activeforeground=bg, command=lambda: submit_number("/"))
multiply_button = tkinter.Button(button_frame, text='*', font=button_font, fg=green, bg=cream, bd=0,
                                 activeforeground=bg, command=lambda: submit_number("*"))
subtract_button = tkinter.Button(button_frame, text='-', font=button_font, fg=green, bg=cream, bd=0,
                                 activeforeground=bg, command=lambda: submit_number("-"))
add_button = tkinter.Button(button_frame, text='+', font=button_font, fg=green, bg=cream, bd=0, activeforeground=bg,
                            command=lambda: submit_number("+"))
equal_button = tkinter.Button(button_frame, text='=', font=button_font, fg=cream, bg=green, bd=0, activeforeground=bg,
                              command=equal)
decimal_button = tkinter.Button(button_frame, text='.', font=button_font, bg=cream, fg=green, bd=0, activeforeground=bg,
                                command=lambda: submit_number("."))
negate_button = tkinter.Button(button_frame, text='+/-', font=button_font, bg=cream, fg=green, bd=0,
                               activeforeground=bg, command=negate)
nine_button = tkinter.Button(button_frame, text='9', font=button_font, bg=cream, fg=green, bd=0, activeforeground=bg,
                             command=lambda: submit_number(9))
eight_button = tkinter.Button(button_frame, text='8', font=button_font, bg=cream, fg=green, bd=0, activeforeground=bg,
                              command=lambda: submit_number(8))
seven_button = tkinter.Button(button_frame, text='7', font=button_font, bg=cream, fg=green, bd=0, activeforeground=bg,
                              command=lambda: submit_number(7))
six_button = tkinter.Button(button_frame, text='6', font=button_font, bg=cream, fg=green, bd=0, activeforeground=bg,
                            command=lambda: submit_number(6))
five_button = tkinter.Button(button_frame, text='5', font=button_font, bg=cream, fg=green, bd=0, activeforeground=bg,
                             command=lambda: submit_number(5))
four_button = tkinter.Button(button_frame, text='4', font=button_font, bg=cream, fg=green, bd=0, activeforeground=bg,
                             command=lambda: submit_number(4))
three_button = tkinter.Button(button_frame, text='3', font=button_font, bg=cream, fg=green, bd=0, activeforeground=bg,
                              command=lambda: submit_number(3))
two_button = tkinter.Button(button_frame, text='2', font=button_font, bg=cream, fg=green, bd=0, activeforeground=bg,
                            command=lambda: submit_number(2))
one_button = tkinter.Button(button_frame, text='1', font=button_font, bg=cream, fg=green, bd=0, activeforeground=bg,
                            command=lambda: submit_number(1))
zero_button = tkinter.Button(button_frame, text='0', font=button_font, bg=cream, fg=green, bd=0, activeforeground=bg,
                             command=lambda: submit_number(0))

# list of buttons for iteration
bt_list = [
    clear_button, quit_button, delete_button, inverse_button, square_button, exponent_button, divide_button,
    seven_button, eight_button, nine_button, multiply_button, four_button, five_button, six_button, subtract_button,
    one_button, two_button, three_button, add_button, negate_button, zero_button, decimal_button, equal_button]

# First row
clear_button.grid(row=0, column=0, columnspan=2, pady=1, padx=1, sticky="WE")
quit_button.grid(row=0, column=3, columnspan=1, pady=1, padx=1, sticky="WE")
delete_button.grid(row=0, column=2, columnspan=1, pady=1, padx=1, sticky="WE")
# Second row
inverse_button.grid(row=1, column=0, pady=1, sticky="WE", padx=1)
square_button.grid(row=1, column=1, pady=1, sticky="WE", padx=1)
exponent_button.grid(row=1, column=2, pady=1, sticky="WE", padx=1)
divide_button.grid(row=1, column=3, pady=1, sticky="WE", padx=1)
# Third row (Add padding to create the size of the columns)
seven_button.grid(row=2, column=0, pady=1, sticky="WE", ipadx=20, padx=1)
eight_button.grid(row=2, column=1, pady=1, sticky="WE", ipadx=20, padx=1)
nine_button.grid(row=2, column=2, pady=1, sticky="WE", ipadx=20, padx=1)
multiply_button.grid(row=2, column=3, pady=1, sticky="WE", ipadx=20, padx=1)
# Fourth row
four_button.grid(row=3, column=0, pady=1, sticky="WE", padx=1)
five_button.grid(row=3, column=1, pady=1, sticky="WE", padx=1)
six_button.grid(row=3, column=2, pady=1, sticky="WE", padx=1)
subtract_button.grid(row=3, column=3, pady=1, sticky="WE", padx=1)
# Fifth row
one_button.grid(row=4, column=0, pady=1, sticky="WE", padx=1)
two_button.grid(row=4, column=1, pady=1, sticky="WE", padx=1)
three_button.grid(row=4, column=2, pady=1, sticky="WE", padx=1)
add_button.grid(row=4, column=3, pady=1, sticky="WE", padx=1)
# Sixth row
negate_button.grid(row=5, column=0, pady=1, sticky="WE", padx=1)
zero_button.grid(row=5, column=1, pady=1, sticky="WE", padx=1)
decimal_button.grid(row=5, column=2, pady=1, sticky="WE", padx=1)
equal_button.grid(row=5, column=3, pady=1, sticky="WE", padx=1)

# Run the root window's main loop
root.mainloop()
