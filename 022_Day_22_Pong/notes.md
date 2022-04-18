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

## Detect Collision with the wall and bounce

Only need to detect a collision on the top and bottom walls. Left and right should be caught by the paddles and if it isn't it's a point to the other side.

When has its position gone passed a wall. How to get the ball to bounce; what does that mean in terms of changing the position of the ball. What happens to the x and y values. Which gets reduced and which stays constant?

---

When the ball is passed 300, it'll be way passed the wall. We'll be sure it'll hit the wall or already has. That's my criteria for detecting collisions.

### main.py
```py
# from paddle import Paddle
# from turtle import Screen, Turtle
# from ball import Ball
# import time

# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
# screen.tracer(0)

# r_paddle = Paddle((350,0))
# l_paddle = Paddle((-350,0))
# ball = Ball()

# screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")

# game_is_on = True
# while game_is_on:
    # time.sleep(0.1)
#   screen.update()
    # ball.move()

    ## DETECT COLLISION WITH WALL
    if ball.ycor() > 300 or ball.ycor() < -300:
      ## NEEDS TO BOUNCE

# screen.exitonclick()
```

### ball.py 
```py
# from turtle import Turtle

# class Ball(Turtle):
#   def __init__(self):
#     super().__init__()
#     self.color("white")
#     self.shape("circle")
#     self.penup()
      self.x_move = 10
      self.y_move = 10

#   def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
#     self.goto(new_x, new_y)

  def bounce(self):
    self.y_move *= -1 
```

### main.py
```py
# from paddle import Paddle
# from turtle import Screen, Turtle
# from ball import Ball
# import time

# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
# screen.tracer(0)

# r_paddle = Paddle((350,0))
# l_paddle = Paddle((-350,0))
# ball = Ball()

# screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")

# game_is_on = True
# while game_is_on:
    # time.sleep(0.1)
#   screen.update()
    # ball.move()

    ## DETECT COLLISION WITH WALL
    if ball.ycor() > 280 or ball.ycor() < -280:
      ## NEEDS TO BOUNCE
      ball.bounce()

# screen.exitonclick()
```

## Detect Collisions with the Paddle

We'd usually use the `distance()` like `ball.distance(paddle)`. Our ball has a width of 20 pixels and so does our paddle. If that distance between the two of them is less than 20, they probably made contact. The problem occurs when the ball hits the edge of the paddle. It measures the center of the ball to the center of the paddle. It won't register as a collision.

Have an additional check -- check its x coordinat and check if it's within 50 pixels of the paddle.

### main.py
```py
    ## DETECT COLLISION WITH WALL
    # if ball.ycor() > 280 or ball.ycor() < -280:
    #   ## NEEDS TO BOUNCE
    #   ball.bounce()

    ##Detect collisio nwith r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
      print("Made contact")

# screen.exitonclick()
```

### ball.py 
```py
# from turtle import Turtle

# class Ball(Turtle):
#   def __init__(self):
#     super().__init__()
#     self.color("white")
#     self.shape("circle")
#     self.penup()
      # self.x_move = 10
      # self.y_move = 10

#   def move(self):
    # new_x = self.xcor() + self.x_move
    # new_y = self.ycor() + self.y_move
#     self.goto(new_x, new_y)

  def bounce_y(self): # REFACTOR; DO SO IN main.py AS WELL
    # self.y_move *= -1 

  def bounce_x(self):
    self.x_move *= -1
```

### main.py
```py
    ## DETECT COLLISION WITH WALL
    # if ball.ycor() > 280 or ball.ycor() < -280:
    #   ## NEEDS TO BOUNCE
      ball.bounce_y()

    ##Detect collisio nwith r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball_distance(l_paddle) < 50 and ball.xcor() < -320:
      # print("Made contact")
      ball.bounce_x()

# screen.exitonclick()
```

## How to Detect when the Ball goes Out of Bounds

If the right paddle misses the ball, left player gets a point; this should trigger a restart of the game and the ball kicks off, going in the opposite direction. Need to check if a ball goes passed a certain part of the screen. If it goes beyond that on the screen, that means its a miss and we should reset the ball.

### main.py
```py
    ## DETECT COLLISION WITH WALL
    # if ball.ycor() > 280 or ball.ycor() < -280:
    #   ## NEEDS TO BOUNCE
      # ball.bounce_y()

    ##Detect collisio with paddle
    # if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball_distance(l_paddle) < 50 and ball.xcor() < -320:
      # print("Made contact")
      # ball.bounce_x()

    ##Detect R paddles misses
    if ball.xcor() > 380:
      ball.reset_position()

    ##Detect L paddle misses
    if ball.xcor() < -380:
      ball.reset_position()

# screen.exitonclick()
```

### ball.py 
```py
# from turtle import Turtle

# class Ball(Turtle):
#   def __init__(self):
#     super().__init__()
#     self.color("white")
#     self.shape("circle")
#     self.penup()
      # self.x_move = 10
      # self.y_move = 10

#   def move(self):
    # new_x = self.xcor() + self.x_move
    # new_y = self.ycor() + self.y_move
#     self.goto(new_x, new_y)

  # def bounce_y(self): # REFACTOR; DO SO IN main.py AS WELL
  #   # self.y_move *= -1 

  # def bounce_x(self):
  #   self.x_move *= -1

  def reset_position(self):
    self.goto(0,0)
    self.bounce_x()
```

## Score Keeping and Changing the Ball Speed

### scoreboard.py
```py
from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    self.update_scoreboard()

  
  def update_scoreboard(self):
    self.goto(-100, 200)
    self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
    self.goto(100, 200)
    self.write(self.r_score, align="center", font=("Courier", 80, "normal"))


  def l_point(self):
    self.l_score += 1
    self.clear()
    self.update_scoreboard()


  def r_point(self):
    self.r_score += 1
    self.update_scoreboard()
```

### main.py
```py
# from paddle import Paddle
# from turtle import Screen, Turtle
# from ball import Ball
from scoreboard import Scoreboard
# import time

# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
# screen.tracer(0)

# r_paddle = Paddle((350,0))
# l_paddle = Paddle((-350,0))
# ball = Ball()
scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")

# game_is_on = True
# while game_is_on:
    # time.sleep(0.1)
#   screen.update()
    # ball.move()

    # ## DETECT COLLISION WITH WALL
    # if ball.ycor() > 280 or ball.ycor() < -280:
    #   ## NEEDS TO BOUNCE
    #   ball.bounce_y()

    ##Detect collisio with paddle
    # if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
      # print("Made contact")
      # ball.bounce_x()

    # ##Detect R paddles misses
    # if ball.xcor() > 380:
    #   ball.reset_position()
        scoreboard.l_point()

    # ##Detect L paddle misses
    # if ball.xcor() < -380:
    #   ball.reset_position()
        scoreboard.r_point()

# screen.exitonclick()
```