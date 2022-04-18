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
SCORE_FILE_PATH = r'C:\repos\100DaysOfPython\Day_24\my_code\snake_high_score\data.txt'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self._get_score()
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
        self.write(f"Score = {self.score} High Score = {self.high_score}", False, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.sety(0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self._set_score()
        self.score = 0
        self.display_score()

    def _get_score(self):
        with open(SCORE_FILE_PATH) as file:
            persistant_high_score = int(file.read())
            return persistant_high_score

    def _set_score(self):
        self.high_score = self.score
        with open(SCORE_FILE_PATH, mode='w') as file:
            file.write(str(self.high_score))