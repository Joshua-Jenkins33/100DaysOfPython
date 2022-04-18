# Day 28 Tkinter, Dynamic Typing, Pomodoro GUI

## How to work with the Canvas Widget and Add Images to Tkinter

The canvas widget allows you to layer things one on top of another. This lets us place an image onto our canvas and then text on top of that image.

```py
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO_ART = r"C:\repos\100DaysOfPython\Day_28_Tkinter_DynamicTyping_PomodoroGUI\pomodoro\art\tomato.png"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro") # this means tomato in italion
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # Got the height/width numbers from the tomato.png
tomato_img = PhotoImage(file=TOMATO_ART)
canvas.create_image(100, 112, image=tomato_img) # 100 is x coordinate, 112 is y coordinate
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()







window.mainloop()
```

## Challenge -- Complete the Application's UI
Hint 1: use `fg` to color the foreground.
Hint 2: copy-paste the checkmark symbol.
Hint 3: use `grid()` instead of `pack()`.
- Label 1: 0, 1
- Canvas 1: 1, 1
- Start Button: 0, 2
- Reset Button: 2, 2
- Check Label: 1, 3

```py
window = Tk()
window.title("Pomodoro") # this means tomato in italion
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # Got the height/width numbers from the tomato.png
tomato_img = PhotoImage(file=TOMATO_ART)
canvas.create_image(100, 112, image=tomato_img) # 100 is x coordinate, 112 is y coordinate
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

check_label = Label(text="✔", fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)
```

## Add a Count Down Mechanism
Create a countdown mechanism that can do something really simple—going from 5 to 0.

```py
count = 5
while True:
  import time.sleep(1)
  count -= 1
```

The above works great in principle, but we're working in a Graphical User Interface Program; that's relevant because it needs to keep watching the screen. The moment something happens, it has to react. It's "Event Driven." It checks every millisecond if something happened, so it's looping on its own. That means we cannot have another loop going at the same time. 

We have to rethink this. We need to do it differently. In order to keep interactive and intresting applications, you need to have things happen on the screen every so often. We need a timing function—Tkinter already thought of this with the `window.after(1000, someFunctionCall, 3, 5, 8)`

```py
def someFunctionCall(a, b, c):
  print(a)
  print(b)
  print(c)
```

We want this to repeat itself, or "loop". It will need to call itself.
```py
def count_down(count):
  print(count)
  if count > 0:
    window.after(1000, count_down, count - 1)

count_down(5)
```

This is the type of count down we need for Pomodoro.

```py
timer_text = canvas.create_text(100, 30, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# changing text in a canvas is slightly different than doing it in a label

def count_down(count):
  canvas.itemconfig(timer_text, text=count)
  if count > 0:
    window.after(1000, count_down, count - 1)

count_down(5)

canvas = Canvas(...)

count_down(5) # reorder so that canvas is declared before count_down
```

Now we need to create tie the behavior to the start button. We need to add a `start_timer` function.

```py
def start_timer():
  count_down(5)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
```

Now I need to change this command to interpret 5 seconds as 5 minutes. Multiply seconds by 60 to get minutes!

```py
def start_timer():
  count_down(5 * 60)
```

We need to format this now so that appears in a digestible format. No one thinks in seconds greater than 60, so we need to split it up visually into minutes.

```py
import math
def count_down():
  # "01:35"
  
  # 245 / 60 = 4.083 (round down)
  # 245 % 60 = seconds remaining after the minutes have been taken away

  count_min = math.floor(count / 60)
  count_sec = count % 60 # 100 / 60 = 1 and 40 as the remainder

  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    window.after(1000, count_down, count - 1)
```

How do you get it to display `5:00` instead of `5:0`?

We need to learn about Python Dynamic Typing.

## Dynamic Typing Explained

How do you get it to display `5:00` instead of `5:0`?

We need to learn about Python Dynamic Typing.

When there is no remainder from the `count_sec = count % 60`, it will just be equal to `0`.

We could use an `if statement` like so:
```py
count_sec = count % 60
if count_sec == 0:
  count_sec = "00"
```

Some might realize there's something a little crazy going on in this line of code.
> If this variable `count_sec` holds data that is equal to the integer, whole number `0`, and then we're setting it to a STRING, these are completely TWO different data types.

`3 + "4"` is not going to work. We get a TypeError.

`a = 3` has a data type of INT
`a = "Hello"` a is now of data type STR

This is dynamic typing.

Python is unique. On one hand, it is STRONGLY TYPED in the sense that it holds on to the data type of the variable. Types matter; and if you call a function that requires 1 data type and pass it another, it will fail. It knows what type is supposed to go into the function and makes sure you comply.

It is also **dynamically typed**. Even though it knows what data type its variable is and that a function expects, you can also dynamically change the data type.

The above `if statement` code, however, has a bug. Once it drops to below 10 seconds, it doesn't bring in the leading `second 0` until it reaches 00. 

### Challenge: Format the seconds remaining with a leading 0.

```py
count_sec = count % 60
if count_sec < 10:
  count_sec = f"0{count_sec}"
```

## Setting Different Timer Sessions and Values

### Challenge: Reps!

Use the reps variable to count down the appropriate number of seconds. When you run the program the timer needs to switch between counting down the work time and the break time (test with 1 minute rather than 25 mintes).

```py
reps = 0
TEST_MIN = 1*60
def start_timer():
  global reps
  reps += 1
  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60

  #If it's the 8th rep:
  if reps % 8 == 0:
    count_down(long_break_sec)
    timer_label.config(text="Long Break", color=RED) 
  #if it's the 2nd/4th/6th rep:
  elif reps % 2 == 0:
    count_down(short_break_sec)
    timer_label.config(text="Break", color=PINK) 
  #If it's the 1st/3rd/5th/7th rep:
  else:
    count_down(TEST_MIN)
    timer_label.config(text="Work", color=GREEN) 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math
def count_down(count):
  count_min = math.floor(count / 60)
  count_sec = count % 60
  if count_sec < 10:
    count_sec = f"0{count_sec}"

  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    window.after(1000, count_down, count - 1)
  else:
    start_timer()
```

## Adding Checkmarks and Resetting the Application
I want to have the checkmark label start off empty.

```py
# ✔
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)
```

### Challenge: Add one checkmark for every two `reps`

```py
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

import math
def count_down(count):
  count_min = math.floor(count / 60)
  count_sec = count % 60
  if count_sec < 10:
    count_sec = f"0{count_sec}"

  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    window.after(1000, count_down, count - 1)
  else:
    start_timer()
    successful_sessions = math.floor(reps/2)
    check_string = int(successful_sessions)*"✔"
    check_label.config(text=check_string)
```

### Reset Button

```py
timer = None # I have to create this as a global variable
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
  window.after_cancel(timer)
  #timer_text 00:00
  #title_label "Timer"
  #reset check_marks

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

import math
def count_down(count):
  count_min = math.floor(count / 60)
  count_sec = count % 60
  if count_sec < 10:
    count_sec = f"0{count_sec}"

  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count - 1) # in order to cancel this we need to store it in a variable
  else:
    start_timer()
    successful_sessions = reps/2
    check_string = int(successful_sessions)*"✔"
    check_label.config(text=check_string)

# ---------------------------- UI SETUP ------------------------------- #

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)
```

### Challenge: Change the `title_label` to "Timer", reset the checkmarks and pause the timer

```py
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
  global reps
  window.after_cancel(timer)
  canvas.itemconfig(timer_text, text="00:00")
  timer_label.config(text="Timer")
  reps = 0
  check_label.config(text="")
```