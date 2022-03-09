import turtle as t
from paddle import Paddle
from ball import Ball

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
while game_is_on:
  if int(ball.xcor()) in range(-400,401) and int(ball.ycor()) in range(-300,301):
    ball.move()
  screen.update()

screen.exitonclick()


