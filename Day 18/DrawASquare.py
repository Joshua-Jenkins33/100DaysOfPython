from turtle import Turtle, Screen

turtle = Turtle()

x = 0
while x < 4:
# for _ in range(4):
  turtle.forward(100)
  turtle.right(90)
  x += 1

screen = Screen()
screen.exitonclick()