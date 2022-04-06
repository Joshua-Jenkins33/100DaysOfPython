import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_forward, 'w')


while scoreboard.is_game_on:
  time.sleep(0.1)
  screen.update()
  car_manager.create_car()
  car_manager.move()

  if player.check_for_finish_line():
    scoreboard.new_level()
    car_manager.increase_speed()

  for car in car_manager.cars:
    if car.distance(player) < 30:
      scoreboard.game_over()

screen.exitonclick()