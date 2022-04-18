import turtle as t
from random import choice, randint

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0,90,180,270]

tim = t.Turtle()
tim.pensize(15)
tim.speed("fastest")
t.colormode(255)

def random_color():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  return (r,g,b)

for _ in range(200):
  tim.pencolor(random_color())
  tim.forward(30)
  tim.setheading(choice(directions))



screen = t.Screen()
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