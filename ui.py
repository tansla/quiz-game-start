import tkinter
from tkinter import PhotoImage
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self._quiz_brain = quiz_brain
        question, self._correct_answer = self._quiz_brain.next_question()
        self._window = tkinter.Tk()
        self._window.title("Quizzo")
        self._window.config(bg=THEME_COLOR, padx=40, pady=20)

        self._score = tkinter.Label(text=f"Score: {self._quiz_brain.get_score()}", fg="white", font="Arial 20", bg=THEME_COLOR)
        self._score.grid(row=0, column=1)

        self._canvas = tkinter.Canvas(width=300, height=300, bg="white", highlightthickness=0)
        self._question_text = self._canvas.create_text(150, 150, text=question, width=250, justify="center",
                                                       font="Arial 20 italic", fill=THEME_COLOR)
        self._canvas.grid(row=1, column=0, columnspan=2, pady=30)

        image_true = PhotoImage(file="./images/true.png")
        image_false = PhotoImage(file="./images/false.png")
        self._true_button = tkinter.Button(image=image_true, command=self.true_pressed, highlightthickness=0)
        self._true_button.grid(row=3, column=0)
        self._false_button = tkinter.Button(image=image_false, command=self.false_pressed, highlightthickness=0)
        self._false_button.grid(row=3, column=1)

        self._window.mainloop()

    def next_question(self, user_answer):
        if self._quiz_brain.still_has_questions():
            self._quiz_brain.check_answer(user_answer, self._correct_answer)
            question, self._correct_answer = self._quiz_brain.next_question()
            self._score.config(text=f"Score: {self._quiz_brain.get_score()}")
        else:
            question = "The end of quiz"
            self._score.config(text=f"Score: {self._quiz_brain.final_score()}")
        self.write_question(question)

    def true_pressed(self):
        self.next_question("True")

    def false_pressed(self):
        self.next_question("False")

    def write_question(self, new_question):
        self._canvas.itemconfig(self._question_text, text=new_question)