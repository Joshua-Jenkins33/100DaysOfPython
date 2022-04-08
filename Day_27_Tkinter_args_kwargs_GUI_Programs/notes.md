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

Functions that can take any number of arguments.

```py
# Limited Arguments 
def add(n1, n2):
  return n1 + n2

add(n1=5, n2=3)

# Unlimited Arguments
def add(*args): # "args" isn't necessary. The * is the important part; tells the function it can take any number of arguments. 
  for n in args:
    print(n)

add(3, 5, 7, 8)
```

### playground.py

`*args` are a **tuple**.

```py
def add(*args):
  sum = 0
  for n in args:
    sum += n
  return sum

add(3, 6, 3, 3, 10, 3020)
```

`*args` are known as **Unlimited *Positional* Arguments**. Unlimited, unspecified number of inputs. What if we want to refer to our arguments by `name` rather than by `position`?

## **kwargs: Many Keyword Arguments

Unlimited Keyword Arguments!

`kwargs` are a **dictionary!**
```py
def calculate(**kwargs):
  print(kwargs)
  print(type(kwargs))
  # This is one way you can loop through the parameters passed into **kwargs
  for key, value in kwargs.items():
    print(key)
    print(value)

  # This is an alternative way to do the same as above
  print(kwargs["add"]) # this lets me look through all of the inputs and find the ones I want and use them to do something

calculate(add=3, multiply=5)
```

**Cleaned Up `def calculate(**kwargs)`**
```py
def calculate(n, **kwargs):
  n += kwargs["add"]
  n *= kwargs["multiply"]

calculate(n, add=3, multiply=5)
```

### Explaining Tkinter 

```py
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")
```

Tkinter is actually imported from another technology called Tk. Tk has a very different syntax from Python. They took all of the parameters from Tk for Tkinter and turned them into `**kwargs` (or optional keyword arguments). The `.pack()` method doesn't prompt any specific input parameters outside of `**kwargs`. 

### Creating a Class like Tkinter

```py

class Car:
  def __init__(self, **kw):
    self.make = kw["make"]
    self.model = kw["model"]

my_car = Car(make="Nissan", model="GT-R") # no properties like "make" or "model" show up when developing this bit; just **kwargs
print(my_car.model)
```

What if I do the same thing but don't include one of the attributes in my instantiation of the class?
```py

class Car:
  def __init__(self, **kw):
    self.make = kw["make"]
    self.model = kw["model"]

my_car = Car(make="Nissan") # notice that I did not pass in a value for MODEL
print(my_car.model)
```

It breaks our code! How do we bypass this? We use the dictionary's `.get("str")` method! If the value we're getting from the dictionary doesn't exist, then it will just return `None` and not return an error.

### Using .get() in Dictionaries
```py
class Car:
  def __init__(self, **kw):
    self.make = kw.get("make")
    self.model = kw.get("model")
    self.colour = kw.get("colour")
    self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
```

This model was converted from another languages and this so happened to be the most efficient way for them to write/convert it.

Other more pythonic modules, you'll see more box-standard type of code with default values for explicit parameters.

## Optional Arguments, *args and **kwargs Quiz

**Question 1.** What is the output of this code?

```py
    def bar(spam, eggs, toast='yes please!', ham=0):
        print(spam, eggs, toast, ham)
     
    bar(1, 2)
```

**Question 2.** What is the output of this code?

```py
    def bar(spam, eggs, toast='yes please!', ham=0):
        print(spam, eggs, toast, ham)
     
    bar(toast='nah', spam=4, eggs=2)
```

**Question 3.** What is the data type of args?

```py
    def test(*args):
        print(args)
     
    test(1,2,3,5)
```

**Question 4.** What is the output of the code below?

```py
    def test(*args):
        print(args)
     
    test(1,2,3,5)
```

**Question 5.** What is the output of the code below?

```py
    def all_aboard(a, *args, **kw): 
        print(a, args, kw)
     
    all_aboard(4, 7, 3, 0, x=10, y=64)
```
## Buttons, Entry, and Setting Component Options

[Documentation for Tkinter](docs.python.org/3/library/tkinter.html)

Under **Handy Reference** we learn that there are several ways to change the properties of things like Buttons. You can do it at instantiation, access the object's properties and change after instantiation, or access the `.config()` method and pass in the relevant arguments. All of the options are listed [here](tcl.tk/man/tcl8.6/TkCmd/label.htm).

```py
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")

######################### OLD STUFF ABOVE #########################

my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text") # this is how we configure or change the properties of a particular component that we've created

#Button

button = tkinter.Button(text="Click Me") # often, folks will do from tkinter import * to skip the `tkinter.` prefaces
button.pack()
```

### Event Listeners

```py
my_label["text"] = "New Text"
my_label.config(text="New Text") 

#Button

def button_clicked():
  print("I got clicked")

button = tkinter.Button(text="Click Me", command=button_clicked) # It's the name of the function, not calling the function
button.pack()
```

### Challenge: Make the Label Read "Button got clicked" when I click the button.

```py
my_label["text"] = "New Text"

def button_clicked():
  my_label["text"] = "Button got clicked"

button = tkinter.Button(text="Click Me", command=button_clicked) # It's the name of the function, not calling the function
button.pack()
```

### Entry Component

```py
# Entry
input = Entry(width=10)
input.pack()
input.get() # this won't actually get anything as this code is ran before the user has a chance to type any text.

```

#### Challenge: Entry Component
```py
from tkinter import *

my_label = tkinter.Label(text="I Am a Label")
my_label.pack()

input = Entry(width=10)
input.pack()

def get_input():
  my_label.config(text=input.get())

button = Button(text="Submit", command=get_input)
button.pack()
```

## Other Tkinter Widgets: Radiobuttons, Scales, Checkbuttons and more

At this point, we've covered the following:
- Labels
- Buttons
- Entries

Now we'll cover:
- Text Entry
- Spinbox
- Scale
- Checkbutton
- Radiobuttons
- Listbox

### Example Code tkinter Widget Demo

This code has default text in the text entry/entries. Focused the text cursor in the box. 

The `entry.insert(END` has that `END` keyword, which is just an index that allows tkinter to figure out which particular item you're referring to.

The `print(text.get("1.0",` is referring to getting a hold of the text starting at the first line, character 0.

The `spinbox` can have a min and max and call a function by passing it a `command=`

The `checkbox` is tied to a variable parameter. `variable=checked_state` where `checked_state=IntVar()` (`IntVar()` is a Class).

The `listbox` uses a `bind` function to call a particular callback.

```py

from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")
  
#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))
  
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
```

## Tkingter Layout Managers: pack(), place(), and grid()

These layout managers will tell the program how to lay out our components.

**Pack.** Packs each widgets next to each other in a vaguely logical format. Starts at the top and packs it just below the previous one. You can pass in a `side=` variable. It is difficulty to specify a precise position, however. This is why there are others.

**Place.** All about precise positioning. If a widget gets created and is not placed by pack, place, or grid, it won't show up. You've got to keep it within the size of your window, however.
- `my_label.place(x=100,y=200)`
- Downside: It is so specific. Can become a nightmare to manage each widget.

**Grid.** Imagines that your entire project is a grid. This grid system is relative to other components. It will be the first in the grid even if it's on column 5 but it's the only component visible. This is preferred; easies to understand. You can't mix up `grid` and `pack` in the same program.
- `my_label.grid(column=0, row=0)`

```py
from tkinter import *

def button_clicked():
  print("I got clicked")
  new_text = input.get()
  my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="new Text")
my_label.pack()

#Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry
input = Entry(width=10)
print(input.get())
input.pack()
```

### Challenge: Grid Placement, Label 0,0 | Button 1,1 | New Button 2,0 | Entry 3,3

```py
from tkinter import *

def button_clicked():
  print("I got clicked")
  new_text = input.get()
  my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="new Text")
my_label.grid(column=0, row=0)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#NewButton
new_button = Button(text="New Button")
button.grid(column=2,row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)
```

### Adding Padding

Easiest way to do this is for each component in their config.
```py
window.config(padx=20, pady=20)
my_label.config(padx=50, pady=50)
```

## Mile to Kilometers Converter Project

See `.\converter` folder.