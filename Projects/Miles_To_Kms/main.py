import tkinter


def convert_miles_kms():
    miles = int(text_input.get())
    kms = round(miles * 1.60934, 3)
    label_value.config(text=f"{kms}")


window = tkinter.Tk()
window.title(string="Mile to Kms Converter")
window.config(height=200, width=400)
window.config(padx=50, pady=50)

text_input = tkinter.Entry(width=10)
text_input.insert(tkinter.END, string="0")
text_input.grid(row=0, column=1)

label_miles = tkinter.Label(text="Miles")
label_miles.grid(row=0, column=2)

label_text = tkinter.Label(text="is equal to")
label_text.grid(row=1, column=0)

label_value = tkinter.Label(text="0")
label_value.grid(row=1, column=1)

label_kms = tkinter.Label(text="Kms")
label_kms.grid(row=1, column=2)

button_calculate = tkinter.Button(text="Calculate")
button_calculate.config(command=convert_miles_kms)
button_calculate.grid(row=2, column=1)

window.mainloop()
