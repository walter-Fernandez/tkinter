from tkinter import *
window = Tk()
window.title("Simple Calculator")
entry = Entry(window, borderwidth = 6, fg = "black", bg = "yellow", width = 25)
entry.grid(columnspan = 4)

def click_number(number):

    #get() makes numbers show in normal orger
    current = entry.get()
    entry.delete(0, END)
    #str(), you cannot concatenate int().
    entry.insert(0, str(current) + str(number))

def click_sum():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, END)

def click_multiplication():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, END)

def click_divition():
    first_number = entry.get()
    global f_num
    global math
    math = "divition"
    f_num = int(first_number)
    entry.delete(0, END)
def click_subtraction():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, END)

def click_clear():
    entry.delete(0,END)

def click_iqual():
    second_number = entry.get()
    entry.delete(0,END)
    if math == "addition":
       entry.insert(0, f_num + int(second_number))
    if math == "subtraction":
       entry.insert(0, f_num - int(second_number))
    if math == "divition":
       entry.insert(0, f_num / int(second_number))
    if math == "multiplication":
       entry.insert(0, f_num * int(second_number))




#creating button
button_0 = Button(window, text = "0", padx = 20, pady = 5, command = lambda: click_number(0))
button_1 = Button(window, text = "1", padx = 20, pady = 5, command = lambda: click_number(1) )
button_2 = Button(window, text = "2", padx = 20, pady = 5, command = lambda: click_number(2) )
button_3 = Button(window, text = "3", padx = 20, pady = 5, command = lambda: click_number(3) )
button_4 = Button(window, text = "4", padx = 20, pady = 5, command = lambda: click_number(4))
button_5 = Button(window, text = "5", padx = 20, pady = 5, command = lambda: click_number(5) )
button_6 = Button(window, text = "6", padx = 20, pady = 5, command = lambda: click_number(6) )
button_7 = Button(window, text = "7", padx = 20, pady = 5, command = lambda: click_number(7) )
button_8 = Button(window, text = "8", padx = 20, pady = 5, command = lambda: click_number(8) )
button_9 = Button(window, text = "9", padx = 20, pady = 5, command = lambda: click_number(9))
button_clear = Button(window, text = "C", padx = 57, pady = 5, command =  click_clear)
button_add = Button(window, text = "+", padx = 20, pady = 5, command = click_sum)
button_iqual = Button(window, text = "=", padx = 57, pady = 5, command =  click_iqual)
button_divition = Button(window, text = "/", padx = 20, pady = 5, command =  click_divition)
button_multiply = Button(window, text = "*", padx = 21, pady = 5, command = click_multiplication)
button_subtraction = Button(window, text = "-", padx = 20, pady = 5, command = click_subtraction)

#organizing button
button_0.grid(row=1, column=0)
button_1.grid(row=1, column=1)
button_2.grid(row=1, column=2)

button_3.grid(row=2, column=0)
button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)

button_6.grid(row=3, column=0)
button_7.grid(row=3, column=1)
button_8.grid(row=3, column=2)

button_9.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan = 2)

button_add.grid(row=5, column=0)
button_iqual.grid(row=5, column=1, columnspan = 2)

button_divition.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_subtraction.grid(row=6, column=2)




window.mainloop()
