import tkinter
from tkinter import messagebox


def evaluate(self, operand, value1, value2):
    pass


calculator = tkinter.Tk()
calculator.title('Calculator')
calculator.config(height=400, width=800)
calculator.resizable(width=False, height=False)

operation = tkinter.StringVar()
operation.set('+')

input1 = tkinter.Text(master=calculator, height=1, width=20)
input1.grid(row=0, column=0, rowspan=4)

radio_plus = tkinter.Radiobutton(master=calculator, text='+', variable=operation, value='+')
radio_plus.grid(row=0, column=1)

radio_minus = tkinter.Radiobutton(master=calculator, text='-', variable=operation, value='-')
radio_minus.grid(row=1, column=1)

radio_multiply = tkinter.Radiobutton(master=calculator, text='*', variable=operation, value='*')
radio_multiply.grid(row=2, column=1)

radio_divide = tkinter.Radiobutton(master=calculator, text='/', variable=operation, value='/')
radio_divide.grid(row=3, column=1)

input2 = tkinter.Text(master=calculator, height=1, width=20)
input2.grid(row=0, column=2, rowspan=4)

btn_evaluate = tkinter.Button(master=calculator, text="Evaluate", command=evaluate)
btn_evaluate.grid(row=4, column=1)

calculator.mainloop()


