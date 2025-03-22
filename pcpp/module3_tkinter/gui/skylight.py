import tkinter as tk
from tkinter import messagebox


def click(event=None):
    reply = messagebox.askquestion("Quit?", "Are you sure?")
    if reply == "yes":
        skylight.destroy()


skylight = tk.Tk()
skylight.title("Skylight")
button = tk.Button(skylight, text="Bye", command=click)
button.place(x=10, y=10)
skylight.mainloop()
