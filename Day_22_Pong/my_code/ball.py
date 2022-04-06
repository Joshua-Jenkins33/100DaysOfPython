from turtle import Turtle
from random import randint

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.color("white")
    

  def move(self):
    # new_x = self.xcor() + 10
    # new_y = self.ycor() + 10
    # self.goto(new_x, new_y)
    self.forward(10)

  def bounce(self):
    old_heading = self.heading()
    if self.ycor() >= 0:
      if self.xcor() >= 0:
        self.setheading(old_heading-90)
      else:
        self.setheading(old_heading+90)
    else:
      if self.xcor() >= 0:
        self.setheading(old_heading+90)
      else:
        self.setheading(old_heading-90)
    self.forward(10)

  def check_collision(self):
    is_collision = False
    if int(self.ycor()) >= 350 or int(self.ycor()) <= -350:
      is_collision = True
    return is_collision

  def check_passed_paddle(self):
    if self.xcor() >= 450 or self.xcor() <= -450:
      self.reset_to_start()
      self.random_direction()

  def random_direction(self):
    self.setheading(randint(0,360))

  def reset_to_start(self):
      self.home()

  def increase_speed(self, speed):
    speed += 0.1
    return speed
    