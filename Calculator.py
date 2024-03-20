from tkinter import *
from math import *

# Create instance
window = Tk()


# Add a title
window.title("Calculator")

window.configure(bg="gray")

window.resizable(False, False)



def click(operator):
    if operator == ".":
        try:
            result = eval(display.get())
            display.delete(0, END)
            display.insert(0, result)
        except Exception as e:
            display.delete(0, END)
            display.insert(0, "Error: " + str(e))
    else:
        display.insert(END, operator)
        
def equalpress():
    try:
        global i
        expression = display.get()
        expression=expression.replace('^','**')
        result = eval(expression)
        display.delete(0, END)
        display.insert(0, result)
        i = 0
    except:
        display.delete(0, END)
        display.insert(0, "Error")
        i = 0

def clear():
    display.delete(0, END)
    i = 0

# Create display
display = Entry(window, font=('lexend', 20, 'bold'), bd=5, justify=RIGHT)
display.grid(row=0, column=0, columnspan=4)


# Create buttons
button_1 = Button(window, text="1",font=('lexend', 20, 'bold'),bg="darkgray", padx=20, pady=5, command=lambda: click(1))
button_2 = Button(window, text="2",font=('lexend', 20, 'bold'),bg="darkgray", padx=20, pady=5, command=lambda: click(2))
button_3 = Button(window, text="3",font=('lexend', 20, 'bold'),bg="darkgray", padx=20, pady=5, command=lambda: click(3))
button_4 = Button(window, text="4",font=('lexend', 20, 'bold'),bg="darkgray", padx=20, pady=5, command=lambda: click(4))
button_5 = Button(window, text="5",font=('lexend', 20, 'bold'),bg="darkgray", padx=20, pady=5, command=lambda: click(5))
button_6 = Button(window, text="6",font=('lexend', 20, 'bold'),bg="darkgray", padx=20, pady=5, command=lambda: click(6))
button_7 = Button(window, text="7",font=('lexend', 20, 'bold'),bg="darkgray", padx=20, pady=5, command=lambda: click(7))
button_8 = Button(window, text="8",font=('lexend', 20, 'bold'),bg="darkgray", padx=20, pady=5, command=lambda: click(8))
button_9 = Button(window, text="9",font=('lexend', 20, 'bold'),bg="darkgray", padx=20, pady=5, command=lambda: click(9))
button_0 = Button(window, text="0",font=('lexend', 20, 'bold'),bg="darkgray", padx=20, pady=5, command=lambda: click(0))
button_dot = Button(window, text=".",font=('lexend', 20, 'bold'),bg="darkgray", padx=23, pady=5, command=lambda: click("."))
button_add = Button(window, text="+",font=('lexend', 20, 'bold'),bg="darkgray", padx=20, pady=5, command=lambda: click("+"))
button_sub = Button(window, text="-",font=('lexend', 20, 'bold'),bg="darkgray", padx=23.5, pady=5, command=lambda: click("-"))
button_multi = Button(window, text="*",font=('lexend', 20, 'bold'),bg="darkgray", padx=23, pady=5, command=lambda: click("*"))
button_div = Button(window, text="/",font=('lexend', 20, 'bold'),bg="darkgray", padx=25, pady=5, command=lambda: click("/"))
button_equal = Button(window, text="=",font=('lexend', 20, 'bold'),bg="orange", padx=20, pady=5, command=equalpress)
button_pow = Button(window, text="^",font=('lexend', 20, 'bold'),bg="darkgray", padx=20, pady=5, command=lambda:click("^"))
button_clear = Button(window, text="C",font=('lexend', 20, 'bold'),bg="darkgray", padx=17.5, pady=5, command=clear)
button_back = Button(window, text="⌫",font=('lexend', 20, 'bold'),bg="darkgray", padx=9.50, pady=5, command=lambda: display.delete(len(display.get())-1))

# Place buttons on the screen
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=1)
button_dot.grid(row=5, column=2)

button_add.grid(row=3, column=3)
button_sub.grid(row=4, column=3)
button_multi.grid(row=2, column=3)
button_div.grid(row=1, column=3)
button_pow.grid(row=1, column=0)

button_clear.grid(row=1, column=1)
button_back.grid(row=1, column=2)
button_equal.grid(row=5, column=3)

# Run the window loop
window.mainloop()