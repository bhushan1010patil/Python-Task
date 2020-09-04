
from tkinter import *
root = Tk()
root.title("Simple calculator")

e = Entry(root, width=40,  borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_cut():
    # num = e.get()
    # e.delete(0, END)
    # e.insert(0, int(num) // 10)
    num = e.get()
    e.delete(0, END)
    num1 = int(num) // 10
    e.insert(0, num1)

def button_add():
    first_number = e.get()
    global math
    math = 'addition'
    global f_num
    f_num = int(first_number)
    e.delete(0,END)

def button_sub():
    first_number = e.get()
    global math
    math = 'subtraction'
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def button_mul():
    first_number = e.get()
    global math
    math = 'multiplication'
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global math
    math = 'division'
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, f_num + int(second_number))

    if math == 'subtraction':
        e.insert(0, f_num - int(second_number))

    if math == 'multiplication':
        e.insert(0, f_num * int(second_number))

    if math == 'division':
        e.insert(0, f_num / int(second_number))


# define the buttons
# In simple function we cant pass parameter so we will take lamda function.

button_1 = Button(root, text='1', padx=30, pady=15, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=30, pady=15, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=30, pady=15, command=lambda: button_click(3))

button_4 = Button(root, text='4', padx=30, pady=15, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=30, pady=15, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=30, pady=15, command=lambda: button_click(6))

button_7 = Button(root, text='7', padx=30, pady=15, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=30, pady=15, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=30, pady=15, command=lambda: button_click(9))

button_0 = Button(root, text='0', padx=30, pady=15, command=lambda: button_click(0))

button_c = Button(root, text='×', padx=29, pady=15, bg='#E74C3C', fg='white', command=button_cut)
button_additi = Button(root, text='ADD', padx=20, pady=41, bg='#3498DB',fg='white', command=button_add)
button_equal = Button(root, text='=', padx=68, pady=15, bg='#1ABC9C', fg='white', command=button_equal)
button_clear = Button(root, text='Clear', padx=59, pady=15, bg='#E74C3C', fg='white', command=button_clear)

button_substract = Button(root, text='SUB', padx=22, pady=15, bg='#3498DB', fg='white', command=button_sub)
button_multiply = Button(root, text='MUL', padx=20, pady=15, bg='#3498DB', fg='white', command=button_mul)
button_divide = Button(root, text='DIV', padx=23, pady=15, bg='#3498DB', fg='white', command=button_div)



# put the buttons on the screen.

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=1, columnspan=2)


button_c.grid(row=5, column=0)
button_clear.grid(row=5, column=1, columnspan=2)

button_divide.grid(row=1, column=3)
button_multiply.grid(row=2, column=3)
button_substract.grid(row=3, column=3)
button_additi.grid(row=4, column=3, rowspan=2)



root.mainloop()