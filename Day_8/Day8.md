# Day 8

## Creating a Function

```py
# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello!")
    print("My name is the greet function!")
    print("What's yours?")

greet()
```

## Functions with Inputs
```py
# Function that allows for input

def greet_with_name(name):
    print(f"Hello, {name}!")
    print("My name is the greet function!")
    print(f"How do you do, {name}?")

greet_with_name("Angela")
```

Parameter is the NAME of that data. Argument is the value.

## Positional vs. Keyword Arguments

Order matters. Takes the position of the data, looks at arguments, first argument assigned to first parameter, second to second parameter. These are **positional arguments**. This is the default way of calling functions. You get the hints.

```py
# Functions with more than 1 input

def greet_with(name, location):
    print(f'Hello, {name}!')
    print(f'What is it like in {location}?')

greet_with('Angela', 'Chicago')
```

### Positional Arguments

```py
def my_function(a, b, c):
    #Do this with a
    #Then do this with b
    #Finally do this with c

my_function(1,2,3)

# Effectively does this:
a = 1
b = 2
c = 3
```

### Keyword Arguments

```py
def my_function(a, b, c):
    #Do this with a
    #Then do this with b
    #Finally do this with c

my_function(a=1,c=2,b=3)

# Effectively does this:
a = 1
b = 3
c = 2
```

```py
def greet_with(name, location):
    print(f'Hello, {name}!')
    print(f'What is it like in {location}?')

greet_with(location='Chicago', name='Angela')
```