from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
      super().__init__()
      self.move_speed = STARTING_MOVE_DISTANCE
      self.cars = []

    def move(self):
      for car in self.cars:
        car.forward(self.move_speed)
      

    def increase_speed(self):
      self.move_speed += MOVE_INCREMENT

    
    def create_car(self):
      probability = randint(1,5)
      if probability == 1:
        new_car = Car(randint(-200, 200))
        self.cars.append(new_car)


class Car(Turtle):
  def __init__(self, position):
    super().__init__()
    self.car_position = position
    self.shape(name="square")
    self.shapesize(stretch_wid=1, stretch_len=3)
    self.color(choice(COLORS))
    self.penup()
    self.goto(310, self.car_position)
    self.setheading(180)
    