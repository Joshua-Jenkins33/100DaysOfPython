'''
Create an application that lets you press the:
1. `W` = Forwards
2. `S` = Backwards
3. `A` = Counter-Clockwise (Leftwards)
4. `D` = Clockwise (Rightwards)
5. `C` = Clear Drawing and put your turtle in the center
'''

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def fresh_slate():
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=fresh_slate)
screen.exitonclick()