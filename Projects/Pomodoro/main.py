import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    label_mode.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    label_completion.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_mode.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_mode.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        label_mode.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
        label_completion.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title(string="Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

label_mode = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
label_mode.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
background_image = tkinter.PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=background_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

button_start = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(row=2, column=2)

label_completion = tkinter.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label_completion.grid(row=3, column=1)

window.mainloop()
