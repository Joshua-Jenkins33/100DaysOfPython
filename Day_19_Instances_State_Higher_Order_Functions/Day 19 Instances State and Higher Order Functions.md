# Instances, State, and Higher Order Functions

## Python Higher Order Functions & Event Listeners

**Using Screen Events.** The `.listen()` method is important here.


### Function as Inputs
When we use a function as an argument, we don't add the parantheses at the end; paranethes trigger the function to happen there and then. We want this method, onkey(), to listen for when the spacebar is pressed and only when that happens to trigger the `moveforwards` function.

```py
def function_a(something):
    #Do this with something
    #Then do this
    #finally do this

def function_b():
    #Do this
```

**Quick Exmample of Passing a Function into Another Function**

```py
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiplpy(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(n1, n2, func):
    return func(n1, n2)

result = calculator(2, 3, add)
print(result)
```

**Higher Order Function.** A function that can work with other functions. The above **calculator** is a higher order function. Really useful for listening to events and then triggering another function.

While we're on the topic of functions, when you're using methods that you haven't created yourself, like `onKey`, use Keyword Arguments rather than Positional Arguments.


## Make an Etch-A-Sketch App

Create an application that lets you press the:
1. `W` = Forwards
2. `S` = Backwards
3. `A` = Counter-Clockwise (Leftwards)
4. `D` = Clockwise (Rightwards)
5. `C` = Clear Drawing and put your turtle in the center

## Object State and Instances

We want to build a turtle race! Have multiple turtles run along a line.
What if we want to build more turtles?

Class/Blueprint to define what a turtle should appear like, how it should behave and what it should do.
We can construct objects! We have these blueprints so we can make MORE OBJECTS! :D

Timmy and Tommy are separate objects, each their own instance of the Turtle objects, they can act independently of each other. They can have different attributes doing different things. 

### State

The condition of their state, attributes or appearance, but can also have different state based on method calls and timings.

Separate versions of the same object with different state acting separately from one another.

## Understanding the Turtle Coordination System

1. Pop-up — Who will win the race?

## Quiz 11: Turtle Coordinate System Quiz

## Aaaaand, we're off to the races!