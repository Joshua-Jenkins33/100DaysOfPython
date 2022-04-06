from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
  time.sleep(ball.ball_speed)
  screen.update()
  ball.move()

  ## DETECT COLLISION WITH WALL
  if ball.ycor() > 280 or ball.ycor() < -280:
    ## NEEDS TO BOUNCE
    ball.bounce_y()

  ##Detect collisio with paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    print("Made contact")
    ball.bounce_x()

  ##Detect R paddles misses
  if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.l_point()

  ##Detect L paddle misses
  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.r_point()

screen.exitonclick()