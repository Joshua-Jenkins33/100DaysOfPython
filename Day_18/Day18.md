# Day 18 -- Turtle Graphics, Tuples, and Importing Modules

## Modules

Documentation is how you learn!

Google `turtle graphics documentation`; this takes you to a long document that shows you all that you can do with this module.

`turtle.shape(name=None)`

In an ideal world, you'd read the full module. Real world --> Not quite possible. Stack Overflow `turtle graphics change the shape of the turtle`. (Query it in google instead with Stack Overflow included).

`Color` takes in a `tk color specification string`. It uses the `pencolor` method.
- This is short for the module for the tkinter (tk interface), one of the ways you can use Python to create a Graphical User Interface.
- Turtle library uses `tkinter` under the hood to create these graphics.
- [Link](https://trinket.io/docs/colors) to colors

## Read and Understand Documentation!

More or less the purpose of this lesson.

[Turtle Documentation](https://docs.python.org/3/library/turtle.html).

## Importing Modules, Installing Packages, and Working with Aliases

### Basic Import

`import turtle`

`import` = keyword
`turtle` = module

Simple import means a new turtle would require a call of the module name and the name of the class.

```py
import turtle

tim = turtle.Turtle()
```

This is great if you're only using it once or twice. More expressive in terms of the code.

### from...import

`from turtle import Turtle`

This is more convenient if we're using the Turtle class alot! We don't have to keep writing turtle.Turtle()

`from` = keyword
`turtle` = module
`import` = keyword
`Turtle` = Thing in Module

```py
from turtle import Turtle

tim = Turtle()
tom = Turtle()
terry = Turtle() # prevents terry = turtle.Turtle()
```

Good to use if you're calling that class/method/variable three times or more.

### Import Everything

`from turtle import *`

Now you can use everything as if it were in the same file!

#### Advantages


#### Disadvantages

Can make it hard to see where each of these classes or methods come from. It's confusing to see this method somewhere in isolation. It's more obvious when you import a module. How is `choice()` working? Where does it come from? 

GOOD CODE ISN'T WRITTEN LIKE THIS!

### Aliasing Modules

`import turtle as t`

`import` = keyword
`turtle` = Module name
`as` = keyword
`t` = alias name

Aliases are names we define!

```py
import turtle as t
tim = t.Turtle() # t represents the entire module
```

### Installing Modules

Some modules can't just be imported.

`import heroes` -- creates an error; no module named heroes. 

`Turtle` is packaged with the Python Standard Library. A small library of code that contains the basics for you to get started. Easily accessible; very small.

Python Packages are hosted on the internet, much bigger library. Only plug and play whatever it is we need.

PyCharm error sense will install it for you by clicking on the red lightbulb!

```py
import heroes
print(heroes.gen())
```

## Python Tuples

A `tuple` is a data type in python. It has round brackets around it, each item inside are separated by a comma. It's similar in appearance to a `list`. Each item in a tuple are `ordered`.

```py
my_tuple = (1, 3, 8)

my_tuple[0] # -- grabs the position; 0 grabs value 1
```

### Why do I need tuples?

A `tuple` is carved in stone; you can't change the values like you can with lists.

```py
my_tuple[2] = 12
```

'tuple' object does not support item assignment. Once you've created your tuple, it is immutable. It cannot be changed.

**Why use it?**
You want the list to remain constant and you don't want someone to change it.

```py
list(my_tuple)
```

The above command lets you change your tuple by accessing it.

---

# Day 18 Project: Hirst Painting

Use the `colorgram.py` module found [here](https://pypi.org/project/colorgram.py/).

Search of `hirst spot painting`