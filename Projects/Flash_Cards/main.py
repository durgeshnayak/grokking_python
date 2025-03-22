import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None


def read_data(file_path):
    data_frame = None
    try:
        data_frame = pandas.read_csv(filepath_or_buffer=file_path)
    except FileNotFoundError:
        data_frame = pandas.read_csv(filepath_or_buffer="./data/german_words.csv")
    finally:
        return data_frame


def convert_data(dataframe):
    dict_word = dataframe.to_dict(orient="records")
    return dict_word


def create_dataframe(dict_word):
    data_frame = pandas.DataFrame.from_dict(dict_word)
    return data_frame


def write_data(dict_word, file_path):
    try:
        dict_word.to_csv(path_or_buf=file_path, index=False)
    except Exception as error:
        print(error)


def get_random_word(words):
    return random.choice(words)


def show_german_word(word):
    global timer
    canvas.itemconfig(tagOrId=title_text, text="German", fill="black")
    canvas.itemconfig(tagOrId=word_text, text=word["German"], fill="black")
    canvas.itemconfig(tagOrId=image_background, image=background_front)
    timer = window.after(3000, flip_card, word)


def show_english_word(word):
    canvas.itemconfig(tagOrId=title_text, text="English", fill="white")
    canvas.itemconfig(tagOrId=word_text, text=word["English"], fill="white")
    canvas.itemconfig(tagOrId=image_background, image=background_back)


def wrong_clicked():
    global word_dict
    global random_word
    df = create_dataframe(word_dict)
    write_data(dict_word=df, file_path="./data/words_to_learn.csv")
    random_word = get_random_word(word_dict)
    show_german_word(random_word)


def right_clicked():
    global word_dict
    global random_word
    word_dict.remove(random_word)
    random_word = get_random_word(word_dict)
    show_german_word(random_word)


def flip_card(word):
    window.after_cancel(timer)
    show_english_word(word)


window = tkinter.Tk()
window.title(string="Flashy Flash Cards")
window.config(padx=50, pady=50)
window.config(background=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

background_front = tkinter.PhotoImage(file="./images/card_front.png")
background_back = tkinter.PhotoImage(file="./images/card_back.png")
image_background = canvas.create_image(400, 263, image=background_front)

title_text = canvas.create_text(400, 175, text="Title", fill="black", font=("Courier", 35, "italic"))
word_text = canvas.create_text(400, 351, text="Word", fill="black", font=("Courier", 50, "bold"))

wrong_background = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=wrong_background, highlightthickness=0, command=wrong_clicked)
wrong_button.grid(row=1, column=0)

right_background = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_background, highlightthickness=0, command=right_clicked)
right_button.grid(row=1, column=1)

word_dict = convert_data(dataframe=read_data(file_path="./data/words_to_learn.csv"))

random_word = get_random_word(word_dict)
show_german_word(random_word)

window.mainloop()
