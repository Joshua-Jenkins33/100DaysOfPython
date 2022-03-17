from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
      super().__init__()
      self.penup()
      self.hideturtle()
      self.level = 1
      self.is_game_on = True
      self.update_scoreboard()

    
    def update_scoreboard(self):
      self.clear()
      self.goto(-250, 250)
      self.write(f"Level {self.level}", align="left", font=FONT)


    def game_over(self):
      self.is_game_on = False
      self.goto(0,0)
      self.write("GAME OVER", align="center", font=FONT)


    def new_level(self):
      self.level += 1
      self.update_scoreboard()