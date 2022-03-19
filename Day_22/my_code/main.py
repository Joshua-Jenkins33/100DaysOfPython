import turtle as t
from paddle import Paddle
from ball import Ball
import time

screen = t.Screen()
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.screensize(canvwidth=800,canvheight=600,bg="black")
screen.title("Pong")

t.listen()

t.onkey(r_paddle.up, "Up")
t.onkey(r_paddle.down, "Down")
t.onkey(l_paddle.up, "w")
t.onkey(l_paddle.down, "s")

game_is_on = True
ball.random_direction()
while game_is_on:
  time.sleep(0.1)
  #if int(ball.xcor()) in range(-400,401) and int(ball.ycor()) in range(-300,301):
  ball.move()

  if ball.check_collision():
    ball.bounce()

  ball.check_passed_paddle()

  if ball.distance(r_paddle) < 15 or ball.distance(l_paddle) < 15:
    ball.bounce()

  screen.update()

screen.exitonclick()


