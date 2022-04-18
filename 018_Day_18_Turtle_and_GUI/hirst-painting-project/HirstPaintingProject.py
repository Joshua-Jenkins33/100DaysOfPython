# import colorgram

# colors = colorgram.extract('hirst.jpg', 30)
# rgb_colors = []

# for color in colors:
#   # rbg_colors.append(color.rgb)
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_color = (r, g, b)
#   rgb_colors.append(new_color)

# print(rgb_colors)

######### we don't need to run the above computation every time; that will slow our program down.

import turtle as t
from random import choice

color_list = [(192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123), (182, 154, 42), (61, 22, 11), (182, 146, 165), (142, 177, 151), (72, 117, 81), (58, 15, 26), (126, 79, 102), (130, 30, 16), (15, 39, 23), (24, 53, 127), (177, 188, 215), (164, 104, 134), (115, 31, 46), (97, 150, 100), (98, 121, 172), (210, 178, 197), (174, 105, 93), (74, 150, 165), (25, 91, 65), (172, 205, 180)]

'''
PROGRAM REQUIREMENTS

10x10 Colored Spots
Dots --> 20 in size
Space --> 50 units
'''

tim = t.Turtle()
tim.hideturtle()
tim.penup()
t.colormode(255)



def move_right():
  tim.forward(50)


def new_line(previous_y_position):
  tim.setpos(0.00, previous_y_position+50)


def draw_dot():
  tim.dot(20, choice(color_list))


def print_dot_line():
  for _ in range(10):
    draw_dot()
    move_right()


for _ in range(10):
  print_dot_line()
  new_line(tim.ycor())


screen = t.Screen()
screen.exitonclick()