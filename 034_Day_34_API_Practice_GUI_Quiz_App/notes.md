# Day 34: Intermediate+ API Practice - Creating a GUI Quiz App
The Trivia API and the Quizzler App. We are going to go back to an API we worked on in Day 17 that has over 3,000 verified questions (Open Trivia Database).

This is a review for what we learned about API Endpoints, sending requests to a particular endpoint to ask for a piece of data. We're also going to be looking at what we learned about API Parameters in order to get different pieces of data from the API. With those, we're going to use Tkinter to build a Quizzler App.

A True/False question shows up in the middle with two buttons for the user to guess the answer.

## Trivia Question API Challenge

We built a question app on Day 17 when we were learning about classes. The goal now, with our newfound knowledge regarding Graphical User Interfaces and the ability to hit APIs, is to upgrade this archaic console app and give it a facelift. And enable it to be more dynamic by drawing data from an API.

`data.py` has a list of dictionary objects. At the time, this was the best we could do (we printed out the API response in the browser and copy/pasted). Hard-coded values will never change. Now, we can take it a step further to get different questions and different answers.

1. Modify the `data.py` file (don't change the `main.py`)
2. Make a `get()` request to fetch 10 True or False questions
3. Parse the JSON response and replace the value of `question_data` (don't change the variable name)

*Hint:* create a Python dictionary for the `amount` and `type` parameters

```py
import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

def get_questions():
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()
    return data['results']

question_data = get_questions()
```

## Solution & Walkthrough for getting Trivia Questions
**Instructor Code**

(Completed it almost word-for-word; just placed mine in a function.)

```py
import requests

parameters = {
  "amount": 10,
  "type": "boolean"
}

response = resposne.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]
```

## Unescaping HTML Entities
Some characters were formatted strangely in the text we were receiving from the API. We were being sent **HTML entities**; it's a way to prevent certain characters from confusing the HTML code. 

We can use [freeformatter.com](https://www.freeformatter.com/html-escape.html) to help for google direction.

Doing so will guide us to the `html` module. We'll want to use this in our `quiz_brain.py` file.

```py
import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
```

This takes you to the `intermediate++` level. Google is your best friend!

## Class based Tkinter UI
Time to upgrade the program so it has a GUI!

### UI.py
We'll be creating our GUI in a class.
```py
from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.mainloop()
```

### main.py
We have to comment out the while loop because the above code has a `window.mainloop()`, a second endless loop. We cannot have two loops going on concurrently.
```py
from ui import QuizInterface

quiz_ui = QuizInterface()

# while quiz.still_has_questions():
#     quiz.next_question()
```

### Challenge: Building Out the GUI

```py
from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            text="Question goes HERE", 
            font=("Arial", 20, "italic"), 
            fill=THEME_COLOR
        )
        self.score_label = Label(text=f"Score: {self.score}", font=("Arial", 12), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        # Paths are relative to the "100DaysOfPython" directory
        true_img = PhotoImage(file=r"034_Day_34_API_Practice_GUI_Quiz_App\quizzler-app-start\images\true.png")
        self.true_button = Button(image=true_img, highlightthickness=0)
        self.true_button.grid(column=0, row=3)
        false_img = PhotoImage(file=r"034_Day_34_API_Practice_GUI_Quiz_App\quizzler-app-start\images\false.png")
        self.false_button = Button(image=false_img, highlightthickness=0)
        self.false_button.grid(column=1, row=3)
        
        self.window.mainloop()

```

## Python Typing & Showing the Next Question in the GUI

We've got the User Interface complete. Now we want to get a hold of new questions! 

QuizBrain, when the method `next_question` was invoked, would find the current question from the list of questions from `data.py` and output that text. Now we want to get ahold of it in our `ui.py`. 

We're going to comment out the part of our code where we check the user_answer, as we aren't getting a `input()` response any longer. We're getting a button click. 

Instead, we're going to get the question text and question number and serve it up as the output.

### QuizBrain.py next_question()
```py
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.questtion_number}: {q_text}"
        #user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        #self.check_answer(user_answer)
```

### ui.py get_next_question()
We need to tap into QuizBrain and call the `next_question()` method. How do we access it? One way is to pass QuizBrain into the QuizInterface (ui). Then we can create a property called `self.quiz = quiz_brain`.

Note that your file doesn't know the data type of this particular object that's being passed in! One of the things you can do is *add* the data type when you add it as a parameter. In order to give it a specific data type of an outside class, you need to import the class.

```py
from quiz_brain import QuizBrain
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        ###

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)      
```

**Calling the Method**
Now we can call the method! But we need to happen during `__init__` so that it starts out displaying a question. But now we can't see the whole question because it's not wrapping.
```py
# self.question_text = self.canvas.create_text(
#             150, 
#             125, 
            width=280,
        #     text="Question goes HERE", 
        #     font=("Arial", 20, "italic"), 
        #     fill=THEME_COLOR
        # )

# self.false_button.grid(row=2, column=1)

self.get_next_question()

#self.window.mainloop()
```
## Python Typing: Type Hints and Arrows ->

### Data Types

1. Integers (int)
2. Strings (str)
3. Decimals (float)
4. Booleans (bool)

We've seen how you can interchange between data types by casting and how data types in Python are flexible, so you can create a variable and change it's data type later on. This is called **Dynamic Typing** as we've previously discussed.

#### Another Thing You Can Do with Data Types
```py
age: int
age = 12 # this age has to match the data type
name: str
height: float
is_human: bool

def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

if police_check(19): # if you put in "twelve" as a string, it throws an error and crashes our app
    print("You may pass.")
else:
    print("Pay a fine.")
```
`->` is used to declare the output!

This is known as a **Type Hint**. Keeps you code safer, less buggy, easier to debug!

## Check the Answer

We need to check the `check_answer()` method. 

Create two new methods that you can add as a `command` to the buttons. The methods need to call `check_answer()` from the `quiz_brain` and pass over the String `"True"` or `"False"`. This should print some feedback to the console.

### ui.py
```py
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_input)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_input)

    def true_input(self):
        self.quiz.check_answer(True)
        self.get_next_question()


    def false_input(self):
        self.quiz.check_answer(False)
        self.get_next_question()
```

### quiz_brain.py
```py
    def check_answer(self, user_answer: bool):
        if user_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
```

## Give Feedback to the Player, Keep Score, and the Fix the Bugs =)
See the feedback on screen! If we guess right, then flash the card green, otherwise flash it red!

Change the canvas' background color to green if `is_right` is `True` and change it to red if `is_right` is `False`. 

When a button has been pressed, display the next question after 1000 milliseconds, but make sure to change the background back to white.

```py
    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(fill="green") # can't mess with the time because of the mainloop
        else:
            self.canvas.config(fill="red")
        self.window.after(1000, command=self.get_next_question)
        self.canvas.config(fill="white")

```

### Scorekeeping
**ui.py**
```py
# def get_next_question(self):
    # self.canvas.config(bg="white")
    self.score_label.config(text=f"Score: " {self.quiz.score})
    # q_text = self.quiz.next_question()
    # self.canvas.itemconfig(self.question_text, text=q_text)
```

### Ending the Quiz
Without the below updates, it fails at the end of the quiz (index out of range).

```py
# def get_next_question(self):
    if self.quiz.still_has_questions():
        # self.canvas.config(bg="white")
        # self.score_label.config(text=f"Score: " {self.quiz.score})
        # q_text = self.quiz.next_question()
        # self.canvas.itemconfig(self.question_text, text=q_text)
    else:
        self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
```

### A Few Ending Bugs
The buttons still change he color when pressed; we want to disable them at the end of the quiz and also make sure the background returns to white.

**Prevent Red/Green Colors from Persisiting.**
```py
# def get_next_question(self):
    self.canvas.config(bg="white") # moving this here makes sure the next question always makes it white.
    # if self.quiz.still_has_questions():
        # self.score_label.config(text=f"Score: " {self.quiz.score})
        # q_text = self.quiz.next_question()
        # self.canvas.itemconfig(self.question_text, text=q_text)
    # else:
        # self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
```

### Finally, get Categorical Questions!

Change `data.py` to get only computer science related questions! We can do this by adding to our API call, a parameter called `category` and set it equal to `18`!