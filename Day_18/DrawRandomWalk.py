from turtle import Turtle, Screen
from random import choice

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim = Turtle()
tim.pensize(10)
tim.pen(speed=8)

def random_direction():
  directions = [0,90,180,270]
  return choice(directions)

x = 0
while x < 200:
  tim.pencolor(choice(colours))
  tim.right(random_direction())
  tim.forward(20)
  x += 1

screen = Screen()
screen.exitonclick()


'''
INSTRUCTOR CODE

import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
time.speed("fastest")

for _ in range(200):
  tim.color(random.choice(colours))
  tim.forward(30)
  tim.setheading(choice(directions))



'''