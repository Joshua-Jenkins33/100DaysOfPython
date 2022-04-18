import turtle as t
from random import randint

tim = t.Turtle()
tim.pensize(1)
tim.speed("fastest")
t.colormode(255)

def random_color():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  return (r,g,b)

for _ in range(45):
  tim.pencolor(random_color())
  tim.circle(100)
  tim.setheading(_*8)



screen = t.Screen()
screen.exitonclick()

'''
INSTRUCTOR CODE

import turtle as t
from random import randint

tim = t.Turtle()
tim.pensize(1)
t.colormode(255)

def random_color():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  color = (r,g,b)
  return color


tim.speed("fastest")


tim.color(random_color())
tim.circle(100)
current_heading = tim.heading()
tim.setheading(current_heading + 10)
tim.circle(100)

=========================================

def draw_spirograph(size_of_gap):
  # size_of_gap determined by heading
  for _ in range(int(360 / size_of_gap)): # float object can't be used as an integer!
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
'''