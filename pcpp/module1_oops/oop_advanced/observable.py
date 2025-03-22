import tkinter

tk = tkinter.Tk()
bool_var = tkinter.BooleanVar(tk)
double_var = tkinter.DoubleVar(tk)
int_var = tkinter.IntVar(tk)
str_var = tkinter.StringVar(tk)

print(bool_var.get())
print(double_var.get())
print(int_var.get())
print(str_var.get())

