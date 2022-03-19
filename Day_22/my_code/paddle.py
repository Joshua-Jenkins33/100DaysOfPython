from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, coordinate: tuple):
      super().__init__()
      self.penup()
      self.color("white")
      self.setposition(coordinate)
      self.shape(name="square")
      self.right(90)
      self.resizemode("user")
      self.shapesize(stretch_wid=1, stretch_len=5)

  def up(self):
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)


  def down(self):
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)


