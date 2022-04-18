# Dat 6 -- Python Functions & Karel the Robot

## Defining and Calling Python Functions

Functions give us a way to refer lots of instructions at the same time. Give them a single instruction and they'll carry out all the instructions.

```py
print('Hello')
num_char = len('Hello')
print(num_char)

def my_function():
    print('Hello')
    print('Bye')

my_function()
```

### Challenge 1

[Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json)

Make him walk in a square!

```py
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
```

### Hurdle 1

[Hurdle 1](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)

```py
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for x in range(0,6):
    jump()
```

## Indentation

It uses 4 spaces!! Ahh!

## While Loop

 While something is true, do this thing.

 ```py

 number_of_hurdles = 6
 while number_of_hurdles > 0:
     jump()
     number_of_hurdles -= 1
     print(number_of_hurdles)
```

## Hurdle 2

```py
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
  
end = False
while end == False:
    jump()
    if at_goal():
        end = True

'''
while not at_goal():
    jump()
'''
```

## Hurdle 3

```py
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
```

## Hurdle 4

```py

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        move()
    else:
        jump()
```

## Maze

```py
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```