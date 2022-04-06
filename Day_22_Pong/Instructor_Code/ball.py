from turtle import Turtle


class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.penup()
    self.x_move = 10
    self.y_move = 10
    self.ball_speed = 0.1


  def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)


  def bounce_y(self): # REFACTOR; DO SO IN main.py AS WELL
    self.y_move *= -1 


  def bounce_x(self):
    self.x_move *= -1
    self.ball_speed *= 0.9
    self.speed(self.ball_speed)


  def reset_position(self):
    self.goto(0,0)
    self.speed(0.1)
    self.bounce_x()
