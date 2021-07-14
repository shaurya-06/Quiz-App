from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR, width=340, height=600)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, pady=20)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text((150, 125),
                                                     text="Some question text",
                                                     font="Arial 20 italic",
                                                     fill=THEME_COLOR,
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.ture_photo = PhotoImage(file=r"images/true.png")
        self.false_photo = PhotoImage(file=r"images/false.png")
        self.true_button = Button(image=self.ture_photo, width=96, height=95, borderwidth=0, command=self.press_true)
        self.true_button.grid(row=2, column=0, padx=10, pady=20)
        self.false_button = Button(image=self.false_photo, width=96, height=95, borderwidth=0, command=self.press_false)
        self.false_button.grid(row=2, column=1, padx=10, pady=20)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        self.score_label.configure(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.configure(state="disabled")
            self.false_button.configure(state="disabled")

    def press_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def press_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)
