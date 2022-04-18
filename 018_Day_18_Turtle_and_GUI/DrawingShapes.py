from turtle import Turtle, Screen, colormode
from random import randint
# Each color is a random color; each side is 100 in terms of length

# Angle Relationship
## 360 / # of sides

def random_color(turtle_pen):
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  colormode(255)
  turtle_pen.pencolor(r,g,b)

def calc_angle(sides):
  return 360/sides

num_of_sides = [3,4,5,6,7,8,9,10]
t = Turtle()

#TODO: Draw a Triangle
for sides in num_of_sides:
  random_color(t)
  angle = calc_angle(sides)
  side = 0
  while side < sides:
    t.right(angle)
    t.forward(100)
    side += 1

screen = Screen()
screen.exitonclick()

'''
INSTRUCTOR CODE

import turtle as t
import random

tim = t.Turtle()

# num_sides = 5

colours = ["LightSeaGreen", "wheat"]

def draw_shape(num_sides):
  angle = 360 / num_sides
  for _ in range(num_sides):
    tim.forward(100)
    tim.right(angle)

for shape_side_n in range(3, 11):
  timm.color(random.choice(colours))
  draw_shape(shape_side_n)
'''