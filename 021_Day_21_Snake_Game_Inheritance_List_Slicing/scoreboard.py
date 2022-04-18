'''
CHALLENGE

New Scoreboard Class that inherits from the Turtle Class.
It needs to know (a turtle) how to keep track of the score and display it.

Score tracked here. Increased by one every time snake eats a piece of food.

Clear the writing every time you update the score.
'''
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.sety(260)
        self.color("white")
        self.display_score()

    def increase_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.sety(0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)