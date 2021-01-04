from tkinter import Tk, Canvas, Label, Button, PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(
            padx=20,
            pady=20,
            bg=THEME_COLOR,
        )
        self.canvas = Canvas(
            width=300,
            height=250,
            bg="white"
        )
        self.question_text = self.canvas.create_text(
            150, 125,
            width=275,
            text=None,
            font=("Arial", 16, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, columnspan=2, row=1, pady=30)

        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 18)
        )
        self.score_label.grid(column=1, row=0)

        check_image = PhotoImage(file="images/true.png")
        self.check_button = Button(
            image=check_image,
            highlightthickness=0,
            command=self.true_button
        )
        self.check_button.grid(column=0, row=2)

        x_image = PhotoImage(file="images/false.png")
        self.x_button = Button(
            image=x_image,
            highlightthickness=0,
            command=self.false_button
        )
        self.x_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Fetch next question from quiz_brain.py"""
        self.canvas.config(bg="white")
        self.check_button.config(state="active")
        self.x_button.config(state="active")

        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've completed the quiz.\n\n"
                     f"Your score is {self.quiz.score}"
            )

            # Disable buttons:
            self.check_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def true_button(self):
        """Correct answer button"""
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)
        self.x_button.config(state="disabled")

    def false_button(self):
        """Wrong answer button"""
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)
        self.check_button.config(state="disabled")

    def give_feedback(self, is_correct):
        """User answer"""
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(2000, self.get_next_question)

