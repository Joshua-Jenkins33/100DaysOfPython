from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text="Question goes HERE", 
            font=("Arial", 20, "italic"), 
            fill=THEME_COLOR
        )
        self.score_label = Label(text=f"Score: {self.score}", font=("Arial", 12), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        # Paths are relative to the "100DaysOfPython" directory
        true_img = PhotoImage(file=r"034_Day_34_API_Practice_GUI_Quiz_App\quizzler-app-start\images\true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_input)
        self.true_button.grid(column=0, row=3)
        false_img = PhotoImage(file=r"034_Day_34_API_Practice_GUI_Quiz_App\quizzler-app-start\images\false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_input)
        self.false_button.grid(column=1, row=3)

        self.get_next_question()
        
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)  
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def true_input(self):
        self.give_feedback(self.quiz.check_answer(True))


    def false_input(self):
        self.give_feedback(self.quiz.check_answer(False))


    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(fill="green") # can't mess with the time because of the mainloop
        else:
            self.canvas.config(fill="red")
        self.window.after(1000, command=self.get_next_question)
        self.canvas.config(fill="white")

