from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
      super().__init__()
      self.penup()
      self.setheading(90)
      self.shape(name="turtle")
      self.setpos(STARTING_POSITION)

    def move_forward(self):
      self.forward(MOVE_DISTANCE)

    def _reset(self):
      self.setpos(STARTING_POSITION)

    def check_for_finish_line(self):
      if self.ycor() >= FINISH_LINE_Y:
        self._reset()
        return True