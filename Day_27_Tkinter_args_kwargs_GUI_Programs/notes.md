# Day 27 -- Tkinter, *args, **kwargs, and Creating GUI Programs

Graphical User Interfaces! Used Turtle; but we're going to go more in-depth. 

Create labels and buttons, respond to button clicks, etc.

More Advanced Python Functions -- by setting default values, unlimited positional args, unlimited keyword args.

**Purpose of Today's Lession.** Create a little program that calculates miles to kilometers!

## History of GUI and Introduction to Tkinter

### Tkinter Module

It's a GUI!

**G**raphical
**U**ser
**I**nterface

### History

Interesting bits of history. Steve Jobs and Bill Gates law suits for Apple and Windows. Mac had GUI first, sued Microsoft for copying their idea. Microsoft got their idea from Xerox employees; Xerox invented the Ethernet, GUI, and mouse.

## Creating Windows and Labels in Tkinter

```py
import tkinter

window = tkinter.Tk()
# Need to keep the window on the screen.

# while True: -- this loop is already included tkinter
window.mainloop() # this will keep the window on-screen. Needs to be at the END of the program. Everything goes between creating the window and this.

```


[The Packer (Tkinter Documentation)](https://docs.python.org/3/library/tkinter.html#the-packer).

```py
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack() # this places it into the screen and centers it
my_label.pack(side="bottom", expand=True) # you can use this to determine where the label goes 
# The above function does not include a list of available parameters
# The secret lies in the **kw --> Next lesson!

import turtle
tim = Turtle() 
tim.write() # this function shows a list of available parameters



window.mainloop()
```

## Setting Default Values for Optional Arguments inside a Function Header

### Keyword Arguments

These inputs can be provided in any order but must be specified.
```py
def my_function(a, b, c):
  #Do this with a
  #Then do this with b
  #Finally do this with c

my_function(c=3, a=1, b=2)
```

### Arguments with Default Values
What if `a` is going to commonly have a value of `1`, `b` a value of `2`, and `c` a value of `3`? Python has a nice way of handling this—default values!
No inputs required. It will just go along as it did before.
```py
def my_function(a=1, b=2, c=3):
  #Do this with a
  #Then do this with b
  #Finally do this with c

my_function()
my_function(b=5) # this will just change the value of b! a and c will still take on their default values.
```

Turtle Example: `turtle.write()` shows the following:
- self: RawTurtle, arg: object, move: bool=..., align: str=..., font: Tuple[str, int, str]=...
  - The `=...` is trying to tell you that these already have a default value
  - This is why you can declare the `turtle.write("Blah blah blah")` function and just give it a value to `text (the arg object)`, because the other arguments have default values
  - You can override optional values

```py
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24))
my_label.pack(side="left") # how can we use these just by typing them in?


window.mainloop()
```

## Default Values Quiz

**Question 1.** What is the output of this code?
```py
    def foo(a, b=4, c=6): 
        print(a, b, c)
     
    foo(1)
```

**Question 2.** What is the output of this code?

```py
    def foo(a, b=4, c=6): 
        print(a, b, c)
     
    foo(4, 9)
```

**Question 3.** What is the output of this code?

```py
    def foo(a, b=4, c=6): 
        print(a, b, c)
     
    foo(1, 7, 9)
```

**Question 4.** What is the output of this code?

```py
    def foo(a, b=4, c=6):
        print(a, b, c)
     
    foo(20, c=6)
```

## *args: Many Positional Arguments

## **kwargs: Many Keyword Arguments

## Optional Arguments, *args and **kwargs Quiz

## Buttons, Entry, and Setting Component Options

## Other Tkinter Widgets: Radiobuttons, Scales, Checkbuttons and more

## Tkingter Layout Managers: pack(), place(), and grid()

## Mile to Kilometers Converter Project