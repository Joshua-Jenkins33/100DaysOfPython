from turtle import Turtle

FONT = ("Courier", 12, "normal")

class StatesManager(Turtle):
    def __init__(self, text, x, y):
      super().__init__()
      self._state_name = text
      self._x_coordinate = x
      self._y_coordinate = y
      self._place_state()


    def _place_state(self):
      self.hideturtle()
      self.penup()
      self.goto(self._x_coordinate, self._y_coordinate)
      self.write(f"{self._state_name}")
