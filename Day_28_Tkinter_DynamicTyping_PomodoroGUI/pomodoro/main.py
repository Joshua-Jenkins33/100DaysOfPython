from tkinter import *
from turtle import color
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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
  global reps
  window.after_cancel(timer)
  canvas.itemconfig(timer_text, text="00:00")
  timer_label.config(text="Timer")
  reps = 0
  check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
  global reps
  reps += 1
  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60

  #If it's the 8th rep:
  if reps % 8 == 0:
    count_down(long_break_sec)
    timer_label.config(text="Long Break", fg=RED) 
  #if it's the 2nd/4th/6th rep:
  elif reps % 2 == 0:
    count_down(short_break_sec)
    timer_label.config(text="Break", fg=PINK) 
  #If it's the 1st/3rd/5th/7th rep:
  else:
    count_down(WORK_MIN)
    timer_label.config(text="Work", fg=GREEN) 

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
    timer = window.after(1000, count_down, count - 1)
  else:
    start_timer()
    successful_sessions = reps/2
    check_string = int(successful_sessions)*"✔"
    check_label.config(text=check_string)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro") # this means tomato in italion
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # Got the height/width numbers from the tomato.png
tomato_img = PhotoImage(file=TOMATO_ART)
canvas.create_image(100, 112, image=tomato_img) # 100 is x coordinate, 112 is y coordinate
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)


window.mainloop()