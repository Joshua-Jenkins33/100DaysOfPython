# Day 21: Build the Snake Game Part 2

## Inheritance
Create a robot chef and tell it how to:
1. bake()
2. stir()
3. measure()

I need a Pastry Chef! It needs to know what the Chef needs to know; but it also needs a bit extra. You don't want to build this entirely from scratch. You want to inherit from the chef!
1. bake()
2. stir()
3. measure()
4. knead()
5. whisk()

You can inherit **appearance** and also **behavior**. 

```py
class Fish(Animal):
    def __init__(self):
        super().__init__() # get a hold of everything that an Animal has an Is; Initialize everything the Animal Class (super) can do in our Fish Class.
```

### Example

```py
class Animal:
    def __init__(self):
        self.num_eyes = 2
    

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
```

### Detect Collision with Food

Everything Snake related is inside the snake class. Now we're going to make a **Food** class. It's going to know how to render itself as a small circle on the screen. Every time it touches the snake it will disappear and reappear in some random location.

```py
'''
food.py
'''
from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)

'''
main.py
'''
from turtle import Screen
from snake2 import Snake
from food import Food
import time

# ~~~

screen.tracer(0)

snake = Snake()
food = Food()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collisions with food
    if snake.head.distance(food) < 15:
        #print("nom nom nom")
        food.refresh()

'''
food.py
'''
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)

```

### Scoreboard

`turtle.write()` -- Tell it what it should right, its alignment, and its font (name, weight, type).

```py
'''
scoreboard.py
'''
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.sety(260)
        self.color("white")
        self.display_score()

    def increase_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT)

'''
main.py
'''
snake = Snake()
food = Food()
scoreboard = Scoreboard()

    # Detect collisions with food
    if snake.head.distance(food) < 15:
        #print("nom nom nom")
        food.refresh()
        scoreboard.increase_score()
```

## Detect Collisions with the Wall

The **height** and **width** of our canvas is 600x600 or -300 to 300.

280 upper and lower bounds should be sufficient.

```py
'''
scoreboard.py
'''

    def game_over(self):
        self.sety(0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

'''
main.py
'''
    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
```

## Detect Collisions with your own tail

```py
'''
snake2.py
'''
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())

'''
main.py
'''
    # Detect collisions with food
    if snake.head.distance(food) < 15:
        #print("nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

```

## How to Slice Lists & Tuples in Python

She doesn't like how wordy this section of code is!

```py
    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
```

### Slicing is the ANSWER

`piano_keys = ['a','b','c','d','e','f','g']`

We want to slice the list to get only `c, d, e` values.

`piano_keys[2:5]` -- we get a set of items by slicing from position 2 to position 5.

```py
piano_keys = ['a','b','c','d','e','f','g']

print(piano_keys[2:5])
print(piano_keys[2:]) # get the rest of the list starting from position you specified
print(piano_keys[:5]) # get all items up to that position
print(piano_keys[2:5:2]) # third parameter gets the increment (every 2 or three instead)
print(piano_keys[::2]) # beginning to end, skip every second one
print(piano_keys[::-1]) # Read the list backward! This method of slicing also works for tuples!
```

### Answer

```py
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
```
