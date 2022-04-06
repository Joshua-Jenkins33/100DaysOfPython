# Draw a Dashed Line
# Draw a line for 10 paces, gap of 10 paces, solid line for 10 paces
# Repeat 15 times
# Line length doesn't matter; Section length doesn't matter
# Alternating draw/no-draw challenge

from turtle import Turtle, Screen

t = Turtle()

for _ in range(15):
  t.forward(10)
  t.penup()
  t.forward(10)
  t.pendown()


screen = Screen()
screen.exitonclick()