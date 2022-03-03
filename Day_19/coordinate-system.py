from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400) # use keyword arguments so it makes sense!
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will the race? Enter a color: ')
#print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def create_turtle(color_name, position):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color_name)
    turtle.goto(x=-230, y=-position)


y_position = -125
for color in colors:
    create_turtle(color, y_position)
    y_position += 50

for turtle in screen.turtles():
    print(turtle.color()[0])



screen.exitonclick()