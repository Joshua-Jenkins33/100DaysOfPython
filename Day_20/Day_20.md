# Build the Snake Game Part 1: Animation & Coordinates

Breakdown the problem! We'll be handling the first three steps on Day 1 and the last four steps on Day 2.

## 1. Screen Setup and Creating a Snake Body

We will create three squares next to each other on the screen!

### main.py
```py
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600) # keyword arguments to be clearer for the next person who looks at the code so it's a little bit clearer
screen.bgcolor("black")
screen.title("My Snake Game")

# ========================================================================================================================
# THERE'S A BETTER WAY TO DO THIS CHUNK
# ========================================================================================================================

segment_1 = Turtle(shape="square")
segment_1.color("white")

segment_2 = Turtle(shape="square")
segment_2.color("white")
segment_2.goto(-20,0)

segment_3 = Turtle(shape="square")
segment_3.color("white")
segment_3.goto(-40,0)

# ========================================================================================================================
# USE A FOR LOOP
# ========================================================================================================================

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)

screen.exitonclick()
```

## 2. Animating the Snake Segments on Screen

Get it to move across the screen without us doing anything.

```py
import time

screen.tracer(0)

segments = []

for position in starting_positions: # FROM PREVIOUS
    new_segment = Turtle("square") # FROM PREVIOUS
    new_segment.color("white") # FROM PREVIOUS
    new_segment.penup()
    new_segment.goto(position) # FROM PREVIOUS
    segments.append(new_segment)

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    # for seg in segments:
    #     seg.forward(20)
        # screen.update()
        # time.sleep(1)
    # segments[0].left(90)
    # for seg_num in range(start=2, stop=0, step=-1):
    for seg_num in range(len(segments)-1,0,1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(90)

```

At this point, turning becomes an issue.

### Create a Snake Class & Move to OOP

Snake is starting and automatically moves forward with the tail following! Now we're going to have our own class! We'll have a total of three classes:
1. Snake Class
2. Food Class
3. Score Class

Goal is to have `main.py` looking like this:
```py
from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
```

---

#### Snake.py

---

```py
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)


    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)
```

## 3. How to Control the Snake with a Keypress

Use the up, down, and arrow keys to control the snake.

```py
snake = Snake() # OLD CODE

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True # OLD CODE

```

### Create the Methods in the Snake Class

```py
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
```

# Day 2

## 4. Detect Collision with Food

## 5. Create a scoreboard

Write text in our application.

## 6. Detect collision with wall

When the game should end.

## 7. Detect collision with tail