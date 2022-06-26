# Day 54: Introduction to Web Development with Flask

## Understanding Backend Web Development with Python

Three Components:
1. Client
    - User going onto a browser
2. Server
    - Powerful computer hooked up to the internet and on 24/7
3. Database
    - Souped up spreadsheet where you store information related to your program

Analogy of a Restaurant:
1. Front of House (Customers sit)
2. Kitchen (Server)
3. Larder (Database of ingredients)

The server fetches relevenat ingredients from the database (fetches information about your spotify playlist) and the server ships it to the client-side so you see what you see.

## Create your First Web Server with Flask

For Windows, you need to set the Flask environment variable to your file:
`set FLASK_APP=hello.py`

(in bash it is `export FLASK_APP=app.py` and you can verify it's there by doing `printenv FLASK_APP`)

Followed by `flask run` in the terminal.

Click on the link and it'll launch your site in the browser. 

Flask converts the string into full html (inspect element and see your string in a tag!)

### Flask
> "One of the most popular web development frameworks." 

#### Library vs. Framework

Biggest difference:
**Libraries:** You are in full control when you call a method from a library and the control is then returned
**Frameworks:** The code never calls into a framework; instead the framework calls you

## Understand the Command Line on Windows and Mac

The terminal is a powerful tool! Type in commands in the terminal/command line/shell to control your computer.

The Kernal is the core of your operating system. The shell of your operating system refers to your user interface to allow you to interact with the kernal. There are GUI and CLI (command line interface). 

**Why Use the Command Line?** 
- Greater control.
- Easier and faster to do common things

`pwd` = Print Working Directory
`ls`= List (Display contents of directory)
`cd` = Change Directory

Creating a new folder:
`mkdir <name>`

Creating a new file:
`touch <name of file>`

deletes file:
`rm <name of file>` 

Remove Directory:
`rm -rf <name of folder>`; recursively and forcibly removes it. Deletes all subfolders in the folder
The terminal is *very* powerful.
Double check you're in the right folder.


## `__name__` and `__main__`: Special Attributes built into Python+

```py
from flask import Flask
app = Flask(__name__)
print("Hi")
print(app)

@app.route('/')
def hello_world():
    return 'Hello World'
```

What is this `__name__`?

`print(__name__)` will print out `__main__`. It's a special attribute built into python. You can tap into the `__name__` to find out what is the current class, function, method or descriptors name.

Getting `__main__` is telling us that we're executing the code in a particular module; it's run as a script or interactive prompt but it's not run from an imported module. Execute something only if it's running as a script.

You'll often see:
```py
if __name__ == "__main__':
    app.run()
```

This does the exact same thing as if we go into the directory and do `flask run`. We can use our standard way of running and stopping python files.

By providing the `__name__`, flask will check that this is the current file where the app code is located and we're not in fact loading a random module.
If you were to import the `random` module into your code and run `print(random.__name__)` then it would print out `random` (the name of the module), but if it was executing `print(__name__)` then it would display `__main__`.

## Python Functions as First Class Objects: Passing & Nesting Functions
The `@` may be unfamiliar. In this case, `@app.route('/')`, it is effectively determining the URL path. This particular example refers to the Home Page denoted by the `/`. 

The **syntax** is a Python decorator. What is a **decorator**?

### Decorator
You have a bunch of functions in your class or module and you want to add some functionality to each of these functions. You might use a decorator function to do that. You can think of it as a function that will give additional functionality to a function.

A function allows us to have certain packages of functionality, get outputs, etc.

Functions are known as **first-class objects**, which means you can pass a function around as an argument like a string, integer, or float.

```py
def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def dividie(n1, n2):
    return n1/n2

#First-class objects, can be passed around as arguments e.g. int/string/float etc
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(multiply, 2, 3)
print(result) # == 6

result = calculate(add, 2, 3)
print(result) # == 5
```

**Nested Functions**
```py
def outer_function():
    print("I am outer")

    # scope is only accessible in the confines of the outer_function
    def nested_function():
        print("I am inner")

    nested_function()

outer_function()
```

**Returning Functions from Another Function**
```py
def outer_function():
    print("I am outer")

    # scope is only accessible in the confines of the outer_function
    def nested_function():
        print("I am inner")

    return nested_function#() -- GET RID OF THE PARENTHESES

inner_function = outer_function()

inner_function() 
```

## Understanding Python Decorator Functions and the `@` Syntax
Python Decorator Function
```py
def decorator_function(function):
    def wrapper_function():
        function()
    return wrapper_function#no parentheses!
```

A decorator function is just another function that wraps another function and gives that function additional functionality. In this case, we have three functions that we'd like to add a two second delay to. We could import the `time` module and apply `time.sleep(2)` to each function. But we could also handle this with decorator functions!

```py
import time

def say_hello():
    time.sleep(2)
    print("Hello")


def say_bye():
    time.sleep(2)
    print("Bye")


def say_greeting():
    time.sleep(2)
    print("How are you?")

say_hello()
```

Handling the above with decorator functions:
```py
import time

def delay_decorator():
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        # or maybe you want to run it twice! function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

@delay_decorator
def say_greeting():
    print("How are you?")

say_hello()
```

A decorator is a function which wraps another function and gives it some additional functionality or modifies the functionality.
`@` is known as **syntactic sugar**. Some syntax you can write to make it easier to write an alternative line of code. Without `@`, we could do the following:

```py
import time

def delay_decorator():
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        # or maybe you want to run it twice! function()
        #Do something after
    return wrapper_function

def say_greeting():
    print("How are you?")

decorated_function = delay_decorator(say_greeting)
decorated_function()
```

## Create Your Own Python Decorator

### Instructions

`time.time()` will return the current time in seconds since January 1, 1970, 00:00:00

Try running the starting code to see the current time printed.

If you run the code after a while, you'll see a new time printed.

e.g. first run:

1598524371.736911

second run:

1598524436.357875

The time difference = second run - first run

64.62096405029297

(approx 1 minute)

Given the above information, complete the code exercise by printing out the speed it takes to run the fast_function() vs the slow_function(). You will need to complete the speed_calc_decorator() function.

### Expected Output

https://cdn.fs.teachablecdn.com/RlMWIliS5uAHLA2bB2fh

HINT: You can use `function.__name__` to get the name of the function,

[SOLUTION](https://repl.it/@appbrewery/day-54-1-solution)