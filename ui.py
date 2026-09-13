import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_QUIZTXT = ("Arial", 20, "italic")
FONT_SCORETXT = ("Arial", 16)


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain, create_quiz):
        """Create the quiz interface and initialise the current quiz."""
        self.quiz = quiz_brain
        self.create_quiz = create_quiz

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        self.score_text = tk.Label(text="Score: 0", pady=20, padx=20, fg="white", bg=THEME_COLOR, font=FONT_SCORETXT)
        self.score_text.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=350, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            175,
            text="start",
            width=250,
            font=FONT_QUIZTXT,
            fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.true_img = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=self.true_img, highlightthickness=0, pady=20, command=self.button_true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_img = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=self.false_img, highlightthickness=0, pady=20, command=self.button_false_pressed)
        self.false_button.grid(row=2, column=1)

        self.new_quiz_button = tk.Button(
            text="Generate New Quiz",
            font=FONT_SCORETXT,
            command=self.generate_new_quiz,
            state="disabled"
        )
        self.new_quiz_button.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=20,
            sticky="ew"
        )

        self.get_next_question()
        self.window.mainloop()

    def generate_new_quiz(self):
        """Generate a new quiz and reset the quiz interface."""

        self.quiz = self.create_quiz()

        self.score_text.config(text="Score: 0")
        self.canvas.config(bg="white")

        self.true_button.config(state="normal")
        self.false_button.config(state="normal")

        self.new_quiz_button.config(state="disabled")

        self.get_next_question()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.score_text.config(text=f"Score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.new_quiz_button.config(state="normal")

    def button_false_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="False"))

    def button_true_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def give_feedback(self, got_it_right):
        if got_it_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)

