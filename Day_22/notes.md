# Day 22 -- Intermediate -- Build Pong: The Famous Arcade Game

## How Might You Structure the Code for this Game?

```py
class Scoreboard():
  def __init__():
    pass

class Paddle():
  pass

class PongBall():
  pass

```

## Code Structure

1. Create the screen
2. Create and move a paddle
3. Create another paddle
4. Create the ball and make it move across the screen
5. Detect collision with the wall and bounce
6. Detect collision with paddle
7. Detect when paddle misses
8. Keep score

## Set up the Main Screen

Create the starting screen! 
- Height of 600 pixels
- Width of 800 pixels
- Black background
- Stays until we click

```py
from turtle import Turtle, Screen

screen = Screen()
screen.screensize(canvwidth=800,canvheight=600,bg="black")
screen.title("Pong")
screen.exitonclick()
```

## Create and Move a Paddle

Create the Right Paddle:
- Width = 20
- Height = 100
- x_pos = 350
- y_pos = 0

We should be able to click the up and down keys on the keyboard to move the paddle.

```py
# from turtle import Screen, Turtle

# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
# screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapsize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)

def go_up():
  new_y = paddle.ycor() + 20
  paddle.goto(paddle.xcor(), new_y)


def go_down():
  new_y = paddle.ycor() - 20
  paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
  screen.update()

screen.exitonclick()
```

## Write the Paddle Class and Create the Second Paddle
Create another paddle; we don't want to repeat all the code we've written, so we want a separate paddle class.

Create paddle in a paddle class; refactor the code!

### Challenge
```md
Refactor the code. Create a paddle.py file for the Paddle class.
The Paddle class needs to inherit from Turtle.
Paddle objects need to be initialized with a tuple for the X and Y coordinates.
The l_paddle needs to move up and down with the "w" and "s" keys.
```

### paddle.py
```py
'''
paddle.py
'''
from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, position):
      super().__init__()
      self.shape("square")
      self.color("white")
      self.shapesize(stretch_wid=5, stretch_len=1)
      self.penup()
      self.goto(position)

  
  def go_up(self):
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)


  def go_down(self):
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)
```

### main.py
```py
from paddle import Paddle
# from turtle import Screen, Turtle

# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
# screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

# screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# game_is_on = True
# while game_is_on:
#   screen.update()

# screen.exitonclick()
```

## Write the Ball Class and Make the Ball Move
- width = 20
- height = 20
- x_pos = 0
- y_pos = 0

It's x and y positions will change with every `screen.update()`.

### ball.py
```py
from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.penup()

  def move(self):
    new_x = self.xcor() + 10
    new_y = self.ycor() + 10
    self.goto(new_x, new_y)
```

### main.py
```py
# from paddle import Paddle
# from turtle import Screen, Turtle
from ball import Ball
import time

# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
# screen.tracer(0)

# r_paddle = Paddle((350,0))
# l_paddle = Paddle((-350,0))
ball = Ball()

# screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")

# game_is_on = True
# while game_is_on:
    time.sleep(0.1)
#   screen.update()
    ball.move()

# screen.exitonclick()
```