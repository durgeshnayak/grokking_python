import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = tkinter.Tk()
        self.window.title("Quizzical")
        self.window.config(background=THEME_COLOR)
        self.window.config(padx=20, pady=20)

        self.lbl_score = tkinter.Label()
        self.lbl_score.config(text="Score: 0")
        self.lbl_score.config(foreground="red", font=("Courier", 30, "bold"), background=THEME_COLOR)
        self.lbl_score.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.config(background="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.lbl_question = self.canvas.create_text(150, 125, width=280, text="", fill=THEME_COLOR)
        self.canvas.itemconfig(tagOrId=self.lbl_question, font=("Arial", 20, "italic"), justify="center")

        background_true = tkinter.PhotoImage(file="./images/true.png")
        self.btn_true = tkinter.Button(image=background_true, highlightthickness=0, command=self.true_clicked)
        self.btn_true.grid(row=2, column=0)

        background_false = tkinter.PhotoImage(file="./images/false.png")
        self.btn_false = tkinter.Button(image=background_false, highlightthickness=0, command=self.false_clicked)
        self.btn_false.grid(row=2, column=1)

        if self.quiz.still_has_questions():
            self.update_question(question=self.quiz.next_question())

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        self.update_score(self.quiz.score)
        self.update_question(question=self.quiz.next_question())

    def update_score(self, score):
        self.lbl_score.config(text=f"Score: {score}")

    def update_question(self, question):
        self.canvas.itemconfig(tagOrId=self.lbl_question, text=question)

    def true_clicked(self):
        if self.quiz.still_has_questions():
            self.give_feedback(self.quiz.check_answer(user_answer="true"))

    def false_clicked(self):
        if self.quiz.still_has_questions():
            self.give_feedback(self.quiz.check_answer(user_answer="false"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)
