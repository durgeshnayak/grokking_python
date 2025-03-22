import tkinter
import tkinter.messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


def find_password():
    website = input_website.get()
    try:
        with open(file="data.json", mode="r") as file_stream:
            data = json.load(file_stream)
    except FileNotFoundError:
        tkinter.messagebox.showwarning(title="Password Manager", message="You don't have any saved data.")
    else:
        if website in data.keys():
            user_email = str(data[website]["email"])
            user_password = str(data[website]["password"])
            tkinter.messagebox.showinfo(title="Password Manager", message=f"Email/Username: {user_email} \n Password:{user_password}")
        else:
            tkinter.messagebox.showwarning(title="Password Manager",
                                           message="You have not saved any login information for "
                                                   "this website.")


def generate_password():
    password_list = []

    password_list_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_list_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_list_numbers = [random.choice(numbers) for number in range(nr_numbers)]

    password_list.extend(password_list_letters)
    password_list.extend(password_list_symbols)
    password_list.extend(password_list_numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    input_password.delete(0, tkinter.END)
    input_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data_to_file():
    website = input_website.get()
    email_address = input_email.get()
    password = input_password.get()
    new_data = {website: {
        "email": email_address,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        tkinter.messagebox.showinfo(title=website, message="Please fill in all the details")
    else:
        try:
            with open(file="data.json", mode="r") as file_stream:
                data = json.load(file_stream)

        except FileNotFoundError:
            with open(file="./data.json", mode="w") as file_stream:
                json.dump(obj=new_data, fp=file_stream, indent=4)
        else:
            data.update(new_data)

            with open(file="./data.json", mode="w") as file_stream:
                json.dump(obj=data, fp=file_stream, indent=4)
        finally:
            input_website.delete(0, tkinter.END)
            input_password.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title(string="Password Manager")
# window.minsize(width=240, height=240)
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
background_image = tkinter.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=background_image)
canvas.grid(row=0, column=1)

label_website = tkinter.Label(text="Website:")
label_website.grid(row=1, column=0)

input_website = tkinter.Entry()
# input_website.config(width=35)
input_website.grid(row=1, column=1)
input_website.focus()

button_search = tkinter.Button(text="Search", command=find_password)
button_search.grid(row=1, column=2)

label_email = tkinter.Label(text="Email/Username:")
label_email.grid(row=2, column=0)

input_email = tkinter.Entry()
input_email.config(width=35)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(tkinter.END, "first_name.last_name@email.com")

label_password = tkinter.Label(text="Password:")
label_password.grid(row=3, column=0)

input_password = tkinter.Entry()
input_password.config(width=21)
input_password.grid(row=3, column=1)

button_generate = tkinter.Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2)

button_add = tkinter.Button(text="Add", command=save_data_to_file)
button_add.config(width=36)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
